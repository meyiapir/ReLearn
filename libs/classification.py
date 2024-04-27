import os
from dotenv import load_dotenv
import torch
from transformers import pipeline
from replicate.client import Client

load_dotenv()

replicate = Client(api_token=os.getenv('REPLICATE_API_TOKEN'))


class HuggingClassifier:
    def __init__(self, model_name):
        pipe = pipeline("text-classification", model=model_name)
        self.tokenizer = pipe.tokenizer
        self.model = pipe.model

    def get_sentiment(self, text, mode, return_type='score', aggregate=False):
        # Управление режимами классификаторов
        match mode:
            case 'positive':
                return_type = 'score'
            case 'swear':
                aggregate = True

        """ Calculate sentiment of a text. `return_type` can be 'label', 'score' or 'proba' """
        with torch.no_grad():
            inputs = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True).to(self.model.device)
            proba = torch.sigmoid(self.model(**inputs).logits).cpu().numpy()[0]

        if aggregate:
            return 1 - proba.T[0] * (1 - proba.T[-1])

        if return_type == 'label':
            return self.model.config.id2label[proba.argmax()]
        elif return_type == 'score':
            score = proba.dot([-1, 0, 1])
            proba = round((score+1)/2, 2)

        return proba


class LLamaClassifier:
    def __init__(self, mode):
        with open(f'prompts/{mode}.txt', 'r', encoding='utf-8') as f:
            self.system_prompt = f.read()

    def get_sentiment(self, text):
        counter = 3

        while counter:
            input = {
                "system_prompt": self.system_prompt,
                "prompt": text,
                "prompt_template": f"<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n{self.system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{text}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
                "presence_penalty": 0,
                "frequency_penalty": 0,
                "max_new_tokens": 512,
            }

            content = ''.join(replicate.run(
                    "meta/meta-llama-3-70b-instruct",
                    input=input))

            try:
                print(text)
                print(float(content.strip()))
                return float(content.strip())
            except Exception as e:
                print(str(e))
                counter -= 1

        if not counter:
            return -1

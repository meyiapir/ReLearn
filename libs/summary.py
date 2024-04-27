import replicate


class Summarizer:
    def __init__(self):
        with open(f'prompts/summary.txt', 'r', encoding='utf-8') as f:
            self.system_prompt = f.read()

    def get_sentiment(self, text):
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

        return content.strip()

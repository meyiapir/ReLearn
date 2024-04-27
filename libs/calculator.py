from libs.classification import LLamaClassifier, HuggingClassifier
from libs.complexity import ClassComplexityCalculator


class Calculator:
    def __init__(self, parameter):
        self.parameter = parameter

    def calculate(self, comments, soft_coeff=None):
        match self.parameter:
            case 'complexity':
                return ClassComplexityCalculator.calculate(comments, soft_coeff=soft_coeff)
            case 'positive' | 'swear':
                classifier_name = dict(
                    swear='cointegrated/rubert-tiny-toxicity',
                    positive='cointegrated/rubert-tiny-sentiment-balanced'
                )[self.parameter]

                classifier = HuggingClassifier(classifier_name)
            case 'tech':
                classifier = LLamaClassifier('tech')

        match self.parameter:
            case 'positive' | 'swear':
                comment_scores = list(map(lambda x: classifier.get_sentiment(x[3], self.parameter), comments))
            case 'tech' | 'complexity':
                comment_scores = list(map(lambda x: classifier.get_sentiment(x[3]), comments))

        comment_scores = [x for x in comment_scores if x >= 0]

        return round(sum(comment_scores)/len(comment_scores), 2)
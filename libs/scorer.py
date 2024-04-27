from libs.calculator import Calculator
from libs.summary import Summarizer


def score(comments):
    positive = Calculator('positive')
    swear = Calculator('swear')
    tech = Calculator('tech')
    complexity = Calculator('complexity')

    scores = {}

    for calculator in (positive, swear, tech, complexity):
        param_score = calculator.calculate(comments)
        scores.update({calculator.parameter: param_score})

    summary = Summarizer().get_sentiment('\n'.join(comments))

    scores.update(dict(summary=summary))

    return scores

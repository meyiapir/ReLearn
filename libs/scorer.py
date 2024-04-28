from libs.calculator import Calculator
from libs.summary import Summarizer
from libs.frequency import FrequencyCalculator


def score(comments):
    positive = Calculator('positive')
    swear = Calculator('swear')
    tech = Calculator('tech')
    complexity = Calculator('complexity')

    scores = {}

    for calculator in (positive, swear, tech, complexity):

        param_score = calculator.calculate(comments)
        scores.update({calculator.parameter: param_score})

    active_coeff = FrequencyCalculator.get_active_coeff(comments)

    summary = Summarizer().get_sentiment('\n'.join([comment[3] for comment in comments]))

    total_score = round((scores['complexity']*0.4 + scores['positive']*0.3 + scores['tech']*0.2 + scores['swear']*0.07 + active_coeff*0.03), 2)

    scores.update(dict(summary=summary, total=total_score, active=active_coeff))

    return scores

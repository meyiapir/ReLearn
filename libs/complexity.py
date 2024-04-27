from libs.classification import LLamaClassifier

llama_classifier = LLamaClassifier('complexity')


class ClassComplexityCalculator:
    @classmethod
    def score_comment(cls, comment):
        return 1 - llama_classifier.get_sentiment(comment)

    @classmethod
    def score_comments(cls, comments):
        return list(map(lambda x: cls.score_comment(x[3]), comments))

    @classmethod
    def get_clever_coeff(cls, comment_scores):
        return sum(comment_scores)/len(comment_scores)

    @classmethod
    def get_teacher_score(cls, clever_coeff, soft_coeff):
        '''
        Получаем из коэффициента понимания учеников скор учителя
        Чем больше soft_coeff, тем мягче оценивание труда учителя
        '''
        return round(-((1-clever_coeff) ** soft_coeff) + 1, 2)

    @classmethod
    def calculate(cls, comments, soft_coeff=None):
        soft_coeff = soft_coeff or 0.9
        comment_scores = cls.score_comments(comments)
        comment_scores = [x for x in comment_scores if x >= 0]
        clever_coeff = cls.get_clever_coeff(comment_scores)
        teacher_score = cls.get_teacher_score(clever_coeff, soft_coeff)

        return teacher_score

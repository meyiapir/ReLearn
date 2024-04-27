import time
import math
import datetime


class FrequencyCalculator:
    @classmethod
    def get_lesson_time(cls, comment):
        return time.mktime(datetime.datetime.strptime(comment[1], "%Y-%m-%d, %H:%M").timetuple())
    @classmethod
    def get_active_coeff(cls, comments, n_users=30):
        start_time = cls.get_lesson_time(comments[0])
        current_time = cls.get_lesson_time(comments[-1])
        lesson_duration = current_time - start_time

        active_coeff = (len(comments)/(1+round(lesson_duration/60)))/n_users

        if active_coeff > 1: active_coeff = 1

        return active_coeff


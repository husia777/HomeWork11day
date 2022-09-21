import random
from load_question import *


class Question():
    def __init__(self, question, the_correct_answer, complexity_question, is_the_question_asked=False, user_response=None ):
        self.question = question
        self.complexity_question = complexity_question
        self.is_the_question_asked = is_the_question_asked
        self.user_response = user_response
        self.the_correct_answer = the_correct_answer

    def get_point(self) -> int:
        """
        Функция добавления очков за правильный ответ
        :return: Кол-во очков
        """
        for i in range(len(get_question())):
            complexity = self.complexity_question
        return  int(complexity) * 10



    def is_correct(self) -> bool:
        """
        Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        :return:
        """
        if self.user_response == self.the_correct_answer:
            return True
        else:
            return False


    def build_question(self) -> str:
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f'{self.question}\nСложность: {self.get_point()//10}/5'


    def build_feedback(self, count=0) -> str:
        """
        Возвращает :
        Ответ верный, получено __ баллов
           Возвращает :
        Ответ неверный, верный ответ __
        :return:
        """
        if self.is_correct():
            return f'Ответ верный, получено {self.get_point()} баллов'
        else:
            return f'Ответ неверный, верный ответ {self.the_correct_answer}'

    def list_question(self) -> list:
        self.a, self.b, self.c, self.d, self.e = get_question()
        question = [self.a, self.b, self.c, self.d, self.e]
        random.shuffle(question)
        return question


    def statistic(self , list_points = []) -> int:
        if self.is_correct():
            list_points.append(self.get_point())
        return sum(list_points)


import random
from load_question import get_question
from classQuestion import *



def main(count = 0):
    a = Question(get_question()[0]['q'], get_question()[0]['a'], get_question()[0]['d'])
    b = Question(get_question()[1]['q'], get_question()[1]['a'], get_question()[1]['d'])
    c = Question(get_question()[2]['q'], get_question()[2]['a'], get_question()[2]['d'])
    d = Question(get_question()[3]['q'], get_question()[3]['a'], get_question()[3]['d'])
    e = Question(get_question()[4]['q'], get_question()[4]['a'], get_question()[4]['d'])
    question = [a, b, c, d, e]
    for i in question:
        print(i.build_question())
        i.user_response = input('Введите ваш ответ')
        if i.is_correct():
            count += 1
        print(i.build_feedback())
        s = i.statistic()
    print(f'\nВот и всё!\nОтвечено на {count} вопроса из {len(get_question())} Набрано баллов: {s}')


if __name__ == "__main__":
	main()

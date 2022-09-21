import random
from load_question import get_question
from classQuestion import *

def list_question() -> list:
    question_list = []
    list_q = get_question()
    random.shuffle(list_q)
    for i in range(len(list_q)):
        question_list.append(Question(list_q[i]['q'], list_q[i]['a'], list_q[i]['d']))
    return question_list

def main(count = 0):
    for i in list_question():
        print(i.build_question())
        i.user_response = input('Введите ваш ответ')
        if i.is_correct():
            count += 1
        print(i.build_feedback())
        s = i.statistic()
    print(f'\nВот и всё!\nОтвечено на {count} вопроса из {len(get_question())} Набрано баллов: {s}')


if __name__ == "__main__":
	main()


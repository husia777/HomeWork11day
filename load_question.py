import json
def get_question() -> list[dict[str, str]]:
    """
    Функция считывания слов из файла JSON
    :return:возвращает список словарей с вопросами,ответами и уровнем сложности
    """
    with open('question.json') as file:
        file = json.load(file)
        return file

print(get_question())
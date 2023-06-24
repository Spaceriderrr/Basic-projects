from random import *

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]


def valid_sentence(n):
    if n.isdigit() or len(n) == 0:
        return False
    else:
        return True


main_flag = True

while main_flag:
    print('Welcome, enter the question please!:')
    question = input()
    if not valid_sentence(question):
        print('Enter not only numbers or empty strings')
        continue
    else:
        print(choice(answers))
    while True:
        print('Wanna ask another question?: Y/N')
        temp = input()
        if temp == 'Y':
            break
        elif temp == 'N':
            main_flag = False
            break
        else:
            print('Only "Y" or "N"')
            continue

    continue

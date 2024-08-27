"""
Вход:
Пользователь должен ввести 'правильный' пароль, состоящий из:
цифр, букв латинского алфавита(строчные и прописные) и
специальных символов  special = '_!@#$%^&'.
Всего 4 набора различных символов.
В пароле обязательно должен быть хотя бы один символ из каждого набора.
Длина пароля от 8(мин) до 15(макс) символов включительно.
Максимальное количество попыток ввода неправильного пароля - 5.
Каждый раз выводим номер попытки.
"""

import string as st

SPECIAL = '_!@#$%^&'


def check_password(parol) -> tuple[bool, list]:
    """ check password for 'strong' """
    results = {'Нет цифр': False,
               'Нет символов нижнего регистра': False,
               'Нет верхнего регистра': False,
               'Нет спец символов': False,
               'Длина не в интервале от 8 до 15': False,
               'Есть недопустимые символы': False}

    count_ok_str = 0
    if 8 <= len(parol) <= 15:
        results['Длина не в интервале от 8 до 15'] = True
    for char in parol:
        if char in st.digits:
            results['Нет цифр'] = True
        if char in st.ascii_lowercase:
            results['Нет символов нижнего регистра'] = True
        if char in st.ascii_uppercase:
            results['Нет верхнего регистра'] = True
        if char in SPECIAL:
            results['Нет спец символов'] = True
        if char in st.digits + st.ascii_lowercase + st.ascii_uppercase + SPECIAL:
            count_ok_str += 1
    if count_ok_str == len(parol):
        results['Есть недопустимые символы'] = True

    if sum(results.values()) == len(results.values()):
        return True, ['Все ок, пароль подходит']

    problems = []
    for key, value in results.items():
        if not value:
            problems.append(key)
    return False, problems


def in_out():
    """ input and output function """
    count = 0
    while True:
        if count == 5:
            print('Вы сделали 5 неудачных попыток, программа закрывается')
            break
        password = input('Введите пароль: ')
        vhod = check_password(password)
        if not vhod[0]:
            print('Пароль не подходит, ошибки следующие:')
            print(*vhod[1], sep='\n')
            count += 1
            print(f'Кол-во оставшихся попыток: {5-count}')
            continue
        print(*vhod[1])
        break


if __name__ == '__main__':
    in_out()
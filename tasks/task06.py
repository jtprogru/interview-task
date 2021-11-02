"""
Задача:
Вам дано большое целое число, представленное в виде массива 'digits',
где каждая 'digits[i]' является 'i'-й цифрой целого числа.
Цифры упорядочены от наиболее значимых до наименее значимых в порядке
слева направо. Большое целое число не содержит никаких ведущих нулей.

Найти:
Увеличьте большое целое число на единицу и верните результирующий массив цифр.

Пример:
на вход: digits = [1,2,3]
на выход: [1,2,4]
"""


def solution(digits: list[int]) -> list[int]:
    i = len(digits) - 1
    flag = True

    while flag:
        if i < 0:
            return [1] + digits

        digits[i] += 1

        if digits[i] == 10:
            digits[i] = 0
            flag = True
        else:
            flag = False

        i -= 1

    return digits

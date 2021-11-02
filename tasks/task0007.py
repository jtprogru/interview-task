"""
Задача:

Вам дано большое целое число, представленное в виде массива 'digits',
где каждая 'digits[i]' является 'i'-й цифрой целого числа.
Цифры упорядочены от наиболее значимых до наименее значимых в порядке
слева направо. Большое целое число не содержит никаких ведущих нулей.

Найти:
Увеличьте большое целое число на единицу и верните результирующий массив цифр.

Пример:
на вход: numRows = 5
на выход: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""


def solution(row_count: int) -> list:
    triangle = [[1], [1, 1]]
    if row_count == 1:
        return [[1]]

    for _ in range(2, row_count):
        new_row = [1]

        last_row = triangle[-1]

        for item in range(len(last_row) - 1):
            curr_row_item = last_row[item] + last_row[item + 1]
            new_row.append(curr_row_item)

        new_row.append(1)

        triangle.append(new_row)

    return triangle

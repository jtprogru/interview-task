"""
Задача от Amazon

Задача:
    Дан отсортированный массив чисел 'a' и целое число 'k'

Найти:
    Необходимо найти два числа из массива, в сумме дающие число 'k'

Пример:
    на вход:
        a = [-1, 2, 5, 8]
        k = 7
    на выходе: [2, 5]
"""


def solution(a: list, k: int):
    li = 0
    ri = len(a) - 1
    while li < ri:
        res = a[li] + a[ri]
        if res == k:
            return [a[li], a[ri]]
        if res < k:
            li += 1
        else:
            ri -= 1
    return []

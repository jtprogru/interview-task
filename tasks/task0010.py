"""
Задача от Google

Задача:
    Дан массив чисел 'a' из 'N' элементов.

Найти:
    Необходимо найти для каждого "дня" сколько суток должно пройти
    до более теплого дня.

Пример:
    на вход:
        a = [13, 12, 15, 11, 9, 12, 16]
    на выходе: [2, 1, 4, 2, 1, 1, 0]
"""

from typing import List


def solution(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    hottest = 0
    answer = [0] * n

    for curr_day in range(n - 1, -1, -1):
        current_temp = temperatures[curr_day]
        if current_temp >= hottest:
            hottest = current_temp
            continue
        days = 1
        while temperatures[curr_day + days] <= current_temp:
            days += answer[curr_day + days]
        answer[curr_day] = days

    return answer

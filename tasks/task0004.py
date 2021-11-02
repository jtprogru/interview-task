"""
Задача:
Дается список чисел

Найти:
Вернуть 'True' если список содержит дубликаты и 'False' в противном случае

Пример:
на вход: [0,1,2,3,3,5]
на выход: True
"""


def solution(nums: list) -> bool:
    checker = {}
    for num in nums:
        if num not in checker:
            checker[num] = 1
        else:
            return True
    return False

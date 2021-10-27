"""
Задача:
Дано три отсортированных массива чисел.
Они могут быть как одинаковой, так и разной длинны.
Во всех массивах есть минимум одно общее число.

Найти:
Любое общее число которое есть во всех трех массивах

Пример:
на вход:
    [1, 2, 3, 4, 5, 100],
    [6, 7, 8, 9, 100],
    [10, 20, 21, 22, 23, 24, 100],
на выход: 100
"""


def solution(arr1: list, arr2: list, arr3: list) -> int:
    pointer_arr1 = 0
    pointer_arr2 = 0
    pointer_arr3 = 0

    while True:
        if arr1[pointer_arr1] == arr2[pointer_arr2] and arr2[pointer_arr2] == arr3[pointer_arr3]:
            return arr1[pointer_arr1]

        if arr1[pointer_arr1] > arr2[pointer_arr2]:
            pointer_arr2 += 1
        elif arr2[pointer_arr2] > arr3[pointer_arr3]:
            pointer_arr3 += 1
        elif arr3[pointer_arr3] > arr1[pointer_arr1]:
            pointer_arr1 += 1

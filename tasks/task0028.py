"""
Дается не сортированный массив arr из чисел размера N, надо вернуть второй максимальный элемент массива.
Во всех остальных случаях должен возвращаться None.
Поиск должен осуществляться за один проход.

Пример 1:

Input: arr = [-2, 3, 0, 1, 5]
Output: 3
Пример 2:

Input: arr = [1, 1]
Output: None
"""
from typing import List, Optional


def solution(arr: List[int]) -> Optional[int]:
    if len(set(arr)) == 1:
        return None

    arr = sorted(arr)
    return arr[-2]

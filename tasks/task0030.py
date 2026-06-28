"""
Avito: Merge two list

Дано 2 отсортированных (по возрастанию) массива A и B длины M и N.
Нужно слить их в один отсортированный (по возрастанию) массив,
состоящий из элементов первых двух.

Ввод:
- a = [1, 2, 5]
- b = [1, 2, 3, 4, 6]

Вывод:
- [1, 1, 2, 2, 3, 4, 5, 6]

Оценка:
- M, N - длины массивов A и B
- Оценка по времени - O(M + N)
- Оценка по памяти - O(M + N)
"""

from typing import List


def solution(a: List[int], b: List[int]) -> List[int]:
    i, j = 0, 0
    result: List[int] = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])

    return result

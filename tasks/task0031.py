"""
Avito: Port ranges

Дан диапазон портов `min` и `max`. Также есть список уже занятых портов `busy`.
Нужно написать функцию, возвращающую все диапазоны свободных портов
внутри `min` и `max`.

Ввод:
- min = 30000 - Минимально допустимый порт
- max = 32000 - Максимально допустимый порт
- busy = [30100, 30200, 31111] - Перечисление конкретных занятых портов

Вывод:
- [[30000, 30099], [30101, 30199], [30201, 31110], [31112, 32000]]

Оценка:
- N - длина списка busy
- Оценка по времени - O(N log N) из-за сортировки (O(N), если busy уже отсортирован)
- Оценка по памяти - O(N)
"""

from typing import List


def solution(min_port: int, max_port: int, busy: List[int]) -> List[List[int]]:
    result: List[List[int]] = []
    start = min_port

    for port in sorted(busy):
        if port < min_port or port > max_port:
            continue
        if port > start:
            result.append([start, port - 1])
        start = port + 1

    if start <= max_port:
        result.append([start, max_port])

    return result

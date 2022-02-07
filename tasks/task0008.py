"""
Задача:
Дан отсортированный массив целых чисел 'a', целое число 'k' и индекс элемента 'indx'.

Найти:
Необходимо вернуть в любом порядке 'K' чисел из массива,
которые являются ближайшими по значению к элементу 'a[index]' .

Пример:
на вход:
    a = [10, 15, 20, 50, 55, 78, 91]
    indx = 2
    k = 3

на выход: [10, 15, 50]
"""


def solution(a: list, idx: int, k: int) -> list:
    elem = a[idx]
    result = []
    li = idx - 1
    ri = idx + 1

    while k > 0:
        k -= 1

        if li < 0:
            result.append(a[ri])
            ri += 1
        elif ri > (len(a) - 1):
            result.append(a[li])  # 15, 55
            li -= 1
        else:
            r1 = elem - a[li]  # 20 - 15 = 5
            r2 = a[ri] - elem  # 50 - 20 = 30

            if r1 > r2:
                result.append(a[ri])
                ri += 1

            elif r2 >= r1:
                result.append(a[li])  # 15, 55
                li -= 1

    return sorted(result)

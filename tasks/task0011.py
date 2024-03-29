"""
Задача от Google

Задача:
    Дано двумерное поле размерностью 'm' на 'n' клеток,
    а так же робот, который всегда в начале находится
    в позиции [1, 1].
    Робот за один ход может двигаться только 'Вверх' и 'Вправо'
    и не может двигаться в любые другие направления.
    'Дверь' находится в координатах [m, n]

Найти:
    Необходимо найти количество способов, которыми 'Робот'
    может добраться до 'Двери'.

Пример:
    на вход:
        m = 2
        n = 3
    на выходе: 3
"""


def solution(m: int, n: int) -> int:
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]

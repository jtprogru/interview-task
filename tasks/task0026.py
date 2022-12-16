"""
Дана строка, например "aafbaaaaffc"
Вывести для каждого символа в ней максимальное количество непрерывных повторений этого символа в строке.

Например, результат будет:
a:4
b:1
f:2
c:1
"""


def solution(s: str) -> dict:
    from collections import defaultdict

    max_seq_of_uniq_symbols = defaultdict(int)

    if len(s) == 0:
        return {}

    prev_symbol = s[0]
    seq_count = 0
    for symbol in s:
        if prev_symbol == symbol:
            seq_count += 1
        if seq_count > max_seq_of_uniq_symbols[prev_symbol]:
            max_seq_of_uniq_symbols[prev_symbol] = seq_count
        if prev_symbol != symbol:
            seq_count = 1
            prev_symbol = symbol

            if max_seq_of_uniq_symbols[symbol] == 0:
                max_seq_of_uniq_symbols[symbol] = 1

    return max_seq_of_uniq_symbols

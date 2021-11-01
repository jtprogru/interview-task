"""
Задача:
Дан отсортированный массив чисел 0..N

Найти:
Удалить все дублирующиеся числа не используя set() и вернуть длинну массива без дубликатов

Пример:
на вход: [0,1,2,3,3,5]
на выход: 5
"""


def solution(nums: list) -> int:
    index = len(nums) - 1
    while index > 0:
        if nums[index] == nums[index - 1]:
            nums.pop(index)
        index -= 1
    return len(nums)

import pytest

from tasks.task0020 import solution


@pytest.mark.parametrize(
    "s, result",
    [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1)
    ],
)
def test_task0020_solution(s, result):
    assert solution(s) == result

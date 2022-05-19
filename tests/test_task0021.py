import pytest

from tasks.task0021 import solution


@pytest.mark.parametrize(
    "s, t, result",
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
    ],
)
def test_task0021_solution(s, t, result):
    assert solution(s, t) == result

import pytest

from tasks.task0025 import solution


@pytest.mark.parametrize(
    "s, result",
    [
        ("42", 42),
        ("   -42", -42),
        ("4193 with words", 4193),
    ],
)
def test_task0025_solution(s, result):
    assert solution(s) == result

import pytest

from tasks.task0022 import solution


@pytest.mark.parametrize(
    "s, result",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ],
)
def test_task0022_solution(s, result):
    assert solution(s) == result

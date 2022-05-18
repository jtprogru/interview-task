import pytest

from tasks.task0018 import solution


@pytest.mark.parametrize(
    "s, result",
    [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    ],
)
def test_task0018_solution(s, result):
    solution(s)
    assert s == result

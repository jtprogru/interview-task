import pytest

from tasks.task0023 import solution


@pytest.mark.parametrize(
    "strs, result",
    [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
    ],
)
def test_task0023_solution(strs, result):
    assert solution(strs) == result

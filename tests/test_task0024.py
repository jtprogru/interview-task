import pytest

from tasks.task0024 import solution


@pytest.mark.parametrize(
    "haystack, needle, result",
    [
        ("hello", "ll", 2),
        ("aaaaa", "bba", -1),
        ("aaaaa", "", 0),
        ("a", "a", 0)
    ],
)
def test_task0022_solution(haystack, needle, result):
    assert solution(haystack, needle) == result

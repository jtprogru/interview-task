import pytest

from tasks.task0026 import solution


@pytest.mark.parametrize(
    "s, result",
    [
        ("aafbaaaaffc", {"a": 4, "b": 1, "c": 1, "f": 2}),
        ("aaafffbbaaffcccc", {"a": 3, "b": 2, "c": 4, "f": 3}),
        ("aaaaabccccc", {"a": 5, "b": 1, "c": 5}),
        ("aaaaaaaaaaa", {"a": 11}),
        ("a", {"a": 1}),
    ],
)
def test_task0026_solution(s, result):
    res = solution(s)
    for k in res.keys():
        assert res[k] == result[k]

    assert solution(s) == result

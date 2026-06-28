import pytest

from tasks.task0031 import solution


@pytest.mark.parametrize(
    "min_port, max_port, busy, result",
    [
        (
            30000,
            32000,
            [30100, 30200, 31111],
            [[30000, 30099], [30101, 30199], [30201, 31110], [31112, 32000]],
        ),
        (
            10,
            12,
            [10, 11, 12],
            [],
        ),
        (
            30000,
            32000,
            [],
            [[30000, 32000]],
        ),
        (
            30000,
            32000,
            [30000],
            [[30001, 32000]],
        ),
        (
            30000,
            32000,
            [32000],
            [[30000, 31999]],
        ),
    ],
)
def test_task0031_solution(min_port, max_port, busy, result):
    assert solution(min_port, max_port, busy) == result

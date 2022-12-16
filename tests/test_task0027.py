import pytest

from tasks.task0027 import solution


@pytest.mark.parametrize(
    "n, movement_steps, result",
    [
        (4, ["север 10", "запад 20", "юг 30", "восток 40"], [20, -20]),
        (2, ["север 20", "юг 20"], [0, 0]),
        (3, ["север 10", "восток 10", "север 10"], [10, 20]),
        (
            10,
            [
                "север 10",
                "восток 20",
                "юг 50",
                "запад 20",
                "запад 40",
                "север 30",
                "север 20",
                "юг 5",
                "юг 90",
                "восток 5",
            ],
            [-35, -85],
        ),
    ],
)
def test_task0027_solution(n, movement_steps, result):
    assert solution(n, movement_steps) == result

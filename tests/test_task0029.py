import pytest

from tasks.task0029 import solution


@pytest.mark.parametrize(
    "s, result",
    [
        (" Hello there thanks for trying my Kata", "#HelloThereThanksForTryingMyKata"),
        ("    Hello     World   ", "#HelloWorld"),
        ("", False),
        (
            "Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat",
            False,
        ),
        ("Codewars", "#Codewars"),
        ("Codewars      ", "#Codewars"),
        ("      Codewars", "#Codewars"),
        ("Codewars Is Nice", "#CodewarsIsNice"),
        ("codewars is nice", "#CodewarsIsNice"),
        ("CoDeWaRs is niCe", "#CodewarsIsNice"),
        ("c i n", "#CIN"),
        ("codewars  is  nice", "#CodewarsIsNice"),
    ],
)
def test_task0028_solution(s, result):
    assert solution(s) == result

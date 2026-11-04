import pytest


def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError
    if a == b == c:
        return "равносторонний"
    if a == b or a == c or b == c:
        return "равнобедренный"
    return "разносторонний"


@pytest.mark.parametrize("a, b, c", [(3, 3, 3), (10, 10, 10)])
def test_equilateral(a, b, c):
    assert classify_triangle(a, b, c) == "равносторонний"


@pytest.mark.parametrize("a, b, c", [(5, 5, 3), (5, 3, 5), (3, 5, 5)])
def test_isosceles(a, b, c):
    assert classify_triangle(a, b, c) == "равнобедренный"


@pytest.mark.parametrize("a, b, c", [(3, 4, 5), (6, 7, 8)])
def test_scalene(a, b, c):
    assert classify_triangle(a, b, c) == "разносторонний"


@pytest.mark.parametrize("a, b, c", [(1, 2, 3), (1, 1, 10), (0, 4, 5), (-3, 4, 5)])
def test_not_triangle(a, b, c):
    with pytest.raises(ValueError):
        classify_triangle(a, b, c)

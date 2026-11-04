import pytest


def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError
    return length * width


@pytest.mark.parametrize("length, width, expected", [
    (2, 3, 6),
    (5, 5, 25),
    (10, 1, 10),
    (4, 2.5, 10),
    (1.5, 2, 3),
])
def test_area(length, width, expected):
    assert calculate_area(length, width) == expected


@pytest.mark.parametrize("length, width", [(0, 5), (-2, 3), (4, -1)])
def test_area_error(length, width):
    with pytest.raises(ValueError):
        calculate_area(length, width)

import pytest


def is_even(number):
    if not isinstance(number, int):
        raise TypeError
    return number % 2 == 0


@pytest.mark.parametrize("number, expected", [
    (2, True),
    (7, False),
    (0, True),
    (-4, True),
    (-3, False),
])
def test_is_even(number, expected):
    assert is_even(number) == expected


@pytest.mark.parametrize("number", ["5", 2.5, None])
def test_is_even_error(number):
    with pytest.raises(TypeError):
        is_even(number)

from src import pipeline
import pytest


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (3.0, 10.0, 13),
    ],
)
def test_add(a, b, expected) -> None:
    basic_obj = pipeline.BasicOperations()
    assert basic_obj.add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, -1),
        (3.0, 10.0, -7.0),
        (0,0,0),
        (5, 2, 3)
    ],
)
def test_subtract(a, b, expected):
    basic_obj = pipeline.BasicOperations()
    assert basic_obj.subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (0, 5, 0),
        (4, 0, 0),
        (-2, 3, -6)
    ]
)
def test_multiply(a, b, expected):
    basic_obj = pipeline.BasicOperations()
    assert basic_obj.multiply(a,b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2),
        (5, 0, 0),
        (10, 2, 5),
        (-6, 3, -2)
    ]
)
def test_divide(a, b, expected):
    basic_obj = pipeline.BasicOperations()
    assert basic_obj.divide(a,b) == expected

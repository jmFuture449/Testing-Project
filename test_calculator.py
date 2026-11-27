import pytest

from calculator import Calculator


@pytest.fixture
def calculator():
	return Calculator()


@pytest.mark.parametrize(
	("operation", "left", "right", "expected"),
	[
		("add", 2, 3, 5),
		("sub", 9, 4, 5),
		("mul", 6, 7, 42),
		("div", 8, 2, 4),
	],
)
def test_valid_calculations(calculator, operation, left, right, expected):
	result = getattr(calculator, operation)(left, right)

	assert result == expected


@pytest.mark.parametrize(
	("operation", "left", "right"),
	[
		("add", "2", 3),
		("sub", 9, "4"),
		("mul", 6, None),
		("div", 8, "2"),
	],
)
def test_invalid_calculations_reject_non_integers(
	calculator, operation, left, right
):
	with pytest.raises((TypeError, ValueError)):
		getattr(calculator, operation)(left, right)


def test_division_by_zero_raises_error(calculator):
	with pytest.raises(ZeroDivisionError):
		calculator.div(7, 0)

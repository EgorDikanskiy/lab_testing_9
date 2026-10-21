import pytest

from calculator import Calculator


@pytest.fixture
def calc():
    # новый объект калькулятора для каждого теста
    return Calculator()


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-4, 4, 0),
        (-2, -3, -5),
        (1000000, 2000000, 3000000),
    ],
)
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected


def test_add_float(calc):
    # дробные числа сравниваем приближённо из-за погрешности float
    assert calc.add(0.1, 0.2) == pytest.approx(0.3)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (3, 5, -2),
        (0, 0, 0),
        (-2, -3, 1),
        (2.5, 0.5, 2.0),
    ],
)
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (7, 0, 0),
        (-2, 3, -6),
        (-2, -3, 6),
        (0.5, 4, 2.0),
    ],
)
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2),
        (1, 2, 0.5),
        (-6, 3, -2),
        (0, 5, 0),
        (1, 3, 0.3333333333),
    ],
)
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a", [5, 0, -3, 2.5])
def test_divide_by_zero(calc, a):
    # при делении на ноль метод должен выбросить исключение
    with pytest.raises(ZeroDivisionError) as error:
        calc.divide(a, 0)
    assert str(error.value) == "Деление на ноль невозможно"


@pytest.mark.parametrize("number", [2, 3, 5, 7, 11, 13, 97, 7919])
def test_is_prime_number_true(calc, number):
    assert calc.is_prime_number(number) is True


@pytest.mark.parametrize("number", [-7, 0, 1, 4, 9, 15, 100, 7917, 2.5])
def test_is_prime_number_false(calc, number):
    assert calc.is_prime_number(number) is False

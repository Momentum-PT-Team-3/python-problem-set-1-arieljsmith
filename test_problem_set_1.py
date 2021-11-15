import pytest
import unittest
from problem_set_1 import (
    given_name,
    candies,
    people,
    left_over,
    greeting,
    is_odd,
    is_even,
    fahrenheit_to_celsius,
    fahrenheit_to_kelvin,
    celsius_to_fahrenheit,
    lesser,
    multigreeting,
    gcd,
)


class VariableTest(unittest.TestCase):
    def test_given_name(self):
        assert given_name == "Addison"

    def test_candies(self):
        assert candies == 20

    def test_people(self):
        assert people == 6

    def test_left_over(self):
        assert left_over == 20 % 6


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ("Chase", "Hello, Chase!"),
        ("Ryan", "Hello, Ryan!"),
        ("Kendall", "Hello, Kendall!"),
    ],
)
def test_greeting(input, expected):
    assert greeting(input) == expected


class IsOddTest(unittest.TestCase):
    def test_odd_num_is_odd(self):
        assert is_odd(3)

    def test_even_num_is_not_odd(self):
        assert not is_odd(10)

    def test_negative_num_is_odd(self):
        assert is_odd(-13)

    def test_float_is_not_odd(self):
        assert not is_odd(5.5)


class IsEvenTest(unittest.TestCase):
    def test_odd_num_is_not_even(self):
        assert not is_even(3)

    def test_even_num_is_even(self):
        assert is_even(10)

    def test_negative_num_is_even(self):
        assert is_even(-12)

    def test_float_is_not_even(self):
        assert not is_even(4.4)


@pytest.mark.parametrize(("f_temp", "expected"), [(32, 0), (212, 100), (77, 25)])
def test_fahrenheit_to_celsius(f_temp, expected):
    assert fahrenheit_to_celsius(f_temp) == expected


@pytest.mark.parametrize(("c_temp", "expected"), [(0, 32), (100, 212), (25, 77)])
def test_celsius_to_fahrenheit(c_temp, expected):
    assert celsius_to_fahrenheit(c_temp) == expected


@pytest.mark.parametrize(
    ("f_temp", "expected"),
    [
        (32, 273.15),
        (212, 373.15),
        (-400, 33.15),
    ],
)
def test_fahrenheit_to_kelvin(f_temp, expected):
    assert round(fahrenheit_to_kelvin(f_temp), 2) == expected


@pytest.mark.parametrize(
    ("num1", "num2", "expected"),
    [(1, 2, 1), (2, 1, 1), (-1, 1, -1), (1, -1, -1)],
)
def test_lesser(num1, num2, expected):
    assert lesser(num1, num2) == expected


@pytest.mark.parametrize(
    ("name", "code", "expected"),
    [
        ("Julian", "en", "Hello, Julian!"),
        ("Julian", "es", "¡Hola, Julian!"),
        ("Julian", "fr", "Bonjour, Julian!"),
        ("Julian", "eo", "Saluton, Julian!"),
        ("Julian", "zz", None),
    ],
)
def test_multigreeting(name, code, expected):
    assert multigreeting(name, code) == expected


class Gcd(unittest.TestCase):
    def test_two_equal_numbers(self):
        assert gcd(81, 81) == 81

    def test_two_even_numbers_with_no_other_common_divisors(self):
        assert gcd(14, 26) == 2

    def test_two_numbers_with_a_common_divisor(self):
        assert gcd(48, 18) == 6

import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.calculator import add, subtract, multiply, divide, square


def test_add():
    assert add(2,3) == 6


def test_subtract():
    assert subtract(5,3) == 2


def test_multiply():
    assert multiply(4,2) == 8


def test_divide():
    assert divide(10,2) == 5


def test_square():
    assert square(4) == 16
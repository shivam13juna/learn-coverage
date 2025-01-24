import pytest
from main import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 2) == 3
    assert sub(0, 5) == -5

def test_mul():
    assert mul(3, 4) == 12
    assert mul(-2, 3) == -6

def test_div():
    assert div(10, 2) == 5
    with pytest.raises(ValueError):
        div(5, 0)

# We recommend installing an extension to run python tests.



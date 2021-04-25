
import pytest
from mathlib_TTT import MathlibTTT


def test_add():
    assert MathlibTTT.add(1, 2) == 3
    assert MathlibTTT.add(1500, 500) == 2000
    assert MathlibTTT.add(2, 2) != 5
    assert MathlibTTT.add(-1500, 2000) == 500


def test_sub():
    assert MathlibTTT.sub(1, 2) == -1
    assert MathlibTTT.sub(1500, 500) == 1000
    assert MathlibTTT.sub(2, 2) != 1


def test_mul():
    assert MathlibTTT.mul(2, 2) == 4
    assert MathlibTTT.mul(20, 50) == 1000
    assert MathlibTTT.mul(-4, 5) == -20
    assert MathlibTTT.mul(-4, -4) == 16


def test_div():
    assert MathlibTTT.div(2, 2) == 1
    assert MathlibTTT.div(3, 2) == 1.5
    assert MathlibTTT.div(15, 5) == 3
    with pytest.raises(ValueError):
        MathlibTTT.div(3, 0)


def test_fac():
    assert MathlibTTT.fac(5) == 120
    assert MathlibTTT.fac(4) == 24
    assert MathlibTTT.fac(10) == 3628800
    with pytest.raises(ValueError):
        MathlibTTT.fac(991)
    with pytest.raises(ValueError):
        MathlibTTT.fac(-1)
    with pytest.raises(ValueError):
        MathlibTTT.fac(3.6)


def test_pow():
    assert MathlibTTT.pow(2, 2) == 4
    assert MathlibTTT.pow(2, 3) == 8
    assert MathlibTTT.pow(5, 2) == 25
    assert MathlibTTT.pow(2, 0) == 1
    with pytest.raises(ValueError):
        MathlibTTT.pow(2, 1.53)


def test_root():
    assert MathlibTTT.root(4, 2) == 2
    assert MathlibTTT.root(8, 3) == 2
    assert round(MathlibTTT.root(25, 5), 5) == 1.90365
    with pytest.raises(ValueError):
        MathlibTTT.root(-2, 2)
    with pytest.raises(ValueError):
        MathlibTTT.root(2, -2)


def test_ln():
    assert MathlibTTT.ln(1) == 0
    assert round(MathlibTTT.ln(2), 6) == 0.693147
    with pytest.raises(ValueError):
        MathlibTTT.ln(0)
    with pytest.raises(ValueError):
        MathlibTTT.ln(-5)


 def test_parse():
    x = "5+5" 
    assert MathlibTTT.parse(x) == 10.0
    x = "5-5" 
    assert MathlibTTT.parse(x) == 0.0
    x = "5.5+5.6" 
    assert MathlibTTT.parse(x) == 11.1
    x = "5.4-5.3" 
    assert MathlibTTT.parse(x) == 0.1
    x = "5+5+5-5+5.5+5.6+5.4-5.3" 
    assert MathlibTTT.parse(x) == 21.2
    x = "10+5*6"
    assert MathlibTTT.parse(x) == 40.0
    x = "10-5*6"
    assert MathlibTTT.parse(x) == -20.0
    x = "10-5*6+10"
    assert MathlibTTT.parse(x) == -10.0
    x = "10-1.5*2"
    assert MathlibTTT.parse(x) == 7.0
    x = "10+5*6-10-5*6+10-5*6+10+10-1.5*2"
    assert MathlibTTT.parse(x) == -3.0
    x = "2^3"
    assert MathlibTTT.parse(x) == 8.0
    x = "root(8,3)"
    assert MathlibTTT.parse(x) == 2.0
    x = "ln(1)"
    assert MathlibTTT.parse(x) == 0.0
    x = "2^3+root(8,3)+ln(1)"
    assert MathlibTTT.parse(x) == 10.0

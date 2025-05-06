from cmath import isclose
from quadratic2 import quad


def test_quad_discriminant_positive():
    a, b, c = 1, -3, 2
    r1, r2 = quad(a, b, c)
    assert isclose(r1, 2) or isclose(r2, 2)
    assert isclose(r1, 1) or isclose(r2, 1)


def test_quad_discriminant_zero():
    a, b, c = 1, -2, 1
    r1, r2 = quad(a, b, c)
    assert isclose(r1, 1)
    assert isclose(r2, 1)


def test_quad_discriminant_negative():
    # Test avec discriminant négatif (racines complexes)
    a, b, c = 1, 0, 1  # racines : i et -i
    r1, r2 = quad(a, b, c)
    assert isclose(r1, 1j) or isclose(r2, 1j)
    assert isclose(r1, -1j) or isclose(r2, -1j)

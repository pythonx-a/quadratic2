
from cmath import sqrt

def quad(a, b, c):
    """ Solve quadratic equation. """
    delta = b**2 - 4 * a * c
    return (
        (-b + sqrt(delta)) / (2 * a),
        (-b - sqrt(delta)) / (2 * a)
    )
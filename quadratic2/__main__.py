import click

from . import quad


@click.command
@click.option("-a", required=True, type=float)
@click.option("-b", required=True, type=float)
@click.option("-c", required=True, type=float)
def main(a, b, c):
    """Solve quadratic equation"""
    x1, x2 = quad(a, b, c)
    print(f"x1={x1}, x2={x2}")


main()
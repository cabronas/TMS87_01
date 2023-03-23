"""
Написать функцию по решению квадратных уравнений.
"""
import math


def rootFinder(a, b, d, sign):
    return (-1 * b + (math.sqrt(d) * sign)) / (2 * a)


def descriminator(a, b, c):
    return (b ** 2) - (4 * a * c)


def quadraticSolver(a, b, c):
    d = descriminator(a, b, c)
    if d < 0:
        print("No roots")
    elif d == 0:
        print("x1 = ", rootFinder(a, b, d, 1))
    else:
        print("x1 = ", rootFinder(a, b, d, 1))
        print("x2 = ", rootFinder(a, b, d, -1))


def main():
    quadraticSolver(1, -6, 8)


if __name__ == "__main__":
    main()

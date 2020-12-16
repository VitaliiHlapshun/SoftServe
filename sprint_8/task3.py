import unittest

def quadratic_equation(a, b, c):
    x1 = round(((-b - ((b ** 2) + (4 * (a * c)))**(1/2)) / (2 * a)).real, 1)
    x2 = round(((-b - ((b ** 2) - (4 * (a * c)))**(1/2)) / (2 * a)).real, 1)
    try:
        quadratic_equation(0, 0, 0)
    except ZeroDivisionError:
        print('error')
    return x1, x2


class QuadraticEquationTest(unittest.TestCase):

    def test_quadratic_equation(self):
        self.assertEqual(quadratic_equation(1, 2, 30), -6.6, -1.0)

    def test_d_more_than_zero(self):
        self.assertEqual(quadratic_equation(3, 50, 10), -16.9, 16.5)

    def test_d_less_than_zero(self):
        self.assertEqual(quadratic_equation(5, 3, 3), -1.1, -0.3)

    def test_d_equals_zero(self):
        self.assertRaise(quadratic_equation(0, 0, 0), ZeroDivisionError("error"))

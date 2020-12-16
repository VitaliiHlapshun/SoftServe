"""Task:

Create class Triangle with method get_area() that calculate area of triangle. As input you will have list of 3 sides size
Examples:
triangle = Triangle([3, 3, 3])

Use classes TriangleNotValidArgumentException and TriangleNotExistException

Create class TriangleTest with parametrized unittest for class Triangle
test data:
"""
valid_test_data = [
    ((3, 4, 5), 6.0),
    ((10, 10, 10), 43.30),
    ((6, 7, 8), 20.33),
    ((7, 7, 7), 21.21),
    ((50, 50, 75), 1240.19),
    ((37, 43, 22), 406.99),
    ((26, 25, 3), 36.0),
    ((30, 29, 5), 72.0),
    ((87, 55, 34), 396.0),
    ((120, 109, 13), 396.0),
    ((123, 122, 5), 300.0)
]
not_valid_triangle = [
    (1, 2, 3),
    (1, 1, 2),
    (7, 7, 15),
    (100, 7, 90),
    (17, 18, 35),
    (127, 17, 33),
    (145, 166, 700),
    (1000, 2000, 1),
    (717, 17, 7),
    (0, 7, 7),
    (-7, 7, 7)
]
not_valid_arguments = [
    ('3', 4, 5),
    ('a', 2, 3),
    (7, "str", 7),
    ('1', '1', '1'),
    'string',
    (7, 2),
    (7, 7, 7, 7),
    'str',
    10,
    ('a', 'str', 7)
]

import unittest
from math import sqrt


class TriangleNotValidArgumentException(Exception):
    pass


class TriangleNotExistException(Exception):
    pass


class Triangle:
    def __init__(self, sides):
        self.sides = sides
        self.validate_args()
        self.validate_triangle()

    def validate_args(self):
        if not isinstance(self.sides, list) \
                or len(self.sides) != 3 \
                or [True for i in self.sides if i <= 0] \
                or [True for i in self.sides if not isinstance(i, int)]:
            raise TriangleNotValidArgumentException

    def validate_triangle(self):
        for i in range(3):
            tmp_lst = self.sides.copy()
            if tmp_lst.pop(i) < sum(tmp_lst):
                raise TriangleNotExistException

    def get_area(self):
        p = sum(self.sides)/2
        a, b, c = self.sides
        s = sqrt(p*(p-a)*(p-b)*(p-c))
        return s


class TriangleTest(unittest.TestCase):

    def setUp(self):
        self.triangle = Triangle

    def test_valid_test_data(self):
        for sides, res in valid_test_data:
            self.assertEqual(self.triangle(sides).get_area(), res)

    def test_not_valid_args(self):
        for sides in not_valid_arguments:
            with self.assertRaises(TriangleNotValidArgumentException):
                self.triangle(sides)

    def test_not_valid_triangle(self):
        for sides in not_valid_triangle:
            with self.assertRaises(TriangleNotExistException):
                self.triangle(sides)

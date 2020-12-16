import unittest

class Product:
    pass

class Cart:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    @property
    def discount(self):
        if 2 <= self.count < 5:
            return self.price
        elif  2 <= self.count < 5:
            return self.price * 0.05
        elif  5 <= self.count < 7:
            return self.price * 0.1
        elif  7 <= self.count < 10:
            return self.price * 0.2
        elif  10 <= self.count < 20:
            return self.price * 0.3
        elif  20 <= self.count:
            return self.price * 0.5

class CartTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.purchase_1 = Cart("banan", 30, 5)
        self.purchase_2 = Cart("lemon", 50, 7)

    def tearDown(self):
        print('tearDown\n')

    def test_discount(self):
        print('test_discount')
        self.assertEqual(self.purchase_1, 3.0)
        self.assertEqual(self.purchase_2, 10.0)

if __name__ == '__main__':
    unittest.main()

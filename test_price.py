import unittest

from checkout import Checkout
from rules import RULES


def price(goods):
    co = Checkout(RULES)

    for product in goods:
        co.scan(product)

    return co.total()


class TestPrice(unittest.TestCase):

    def test_totals(self):
        self.assertEqual(0, price(""))
        self.assertEqual(50, price("A"))
        self.assertEqual(80, price("AB"))
        self.assertEqual(115, price("CDBA"))

        self.assertEqual(100, price("AA"))
        self.assertEqual(130, price("AAA"))
        self.assertEqual(180, price("AAAA"))
        self.assertEqual(230, price("AAAAA"))
        self.assertEqual(260, price("AAAAAA"))

        self.assertEqual(160, price("AAAB"))
        self.assertEqual(175, price("AAABB"))
        self.assertEqual(190, price("AAABBD"))
        self.assertEqual(190, price("DABABA"))

    def test_incremental(self):
        co = Checkout(RULES)
        self.assertEqual(0, co.total())
        co.scan("A")
        self.assertEqual(50, co.total())
        co.scan("B")
        self.assertEqual(80, co.total())
        co.scan("A")
        self.assertEqual(130, co.total())
        co.scan("A")
        self.assertEqual(160, co.total())
        co.scan("B")
        self.assertEqual(175, co.total())


if __name__ == '__main__':
    unittest.main()

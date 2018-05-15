from simple_number import SimpleNumber
import unittest

class TestSimpleNumber(unittest.testCase):

    def test_default(self):
        num = SimpleNumber(2)
        self.assertEqual(num.val, 2)

    def test_add(self):
        num = SimpleNumber(2)
        self.assertEqual(num.add(2))

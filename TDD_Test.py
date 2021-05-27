import pytest
import unittest

from TDD_Calc_Functions import Function_Calc

class Calc_Test(unittest.TestCase):  # helps us test

    calc_test = Function_Calc()

    def test_inches(self):
        # this naming convention is essential as 'test' is the word that we need to use when naming tests so python interpreter can recognise it so it can run
        self.assertEqual(self.calc_test.inches(10), 25.4)  # 10 * 2.54 = 25.4

    def test_modular(self):
        self.assertEqual(self.calc_test.modular(4, 2), 0)  # 4 % 2 = 0 | no remainder

    def test_triangle(self):
        self.assertEqual(self.calc_test.triangle(10, 10), 50)  # (height * base) / 2 = 50

    def test_percentage(self):
        self.assertEqual(self.calc_test.percentage(10, 50), 20)  # (10 / 50) * 100 = 20%

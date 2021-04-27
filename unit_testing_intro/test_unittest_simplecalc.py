from simple_calc import SimpleCalc
import unittest
import pytest

class Calctest(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6) # assert that the output of calc.add(2, 4) = 6


    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)


    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 2), 8)


    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(4), 2)

import unittest
import math
from calculator import Calculator


class ApplicationTest(unittest.TestCase):
    calc = Calculator()


    def test_add(self):
        param_list = [(48, 29), (63, 25), (12, 19), (35, 97), (100, 123)]
        for i, j in param_list:
            n = self.calc.add(i, j)
            self.assertEqual(n, i + j)
        self.assertRaises(TypeError, self.calc.add, 99, "121")
        pass


    def test_divide(self):
        param_list = [(48, 29), (63, 25), (12, 19), (35, 97), (100, 123)]
        for i, j in param_list:
            n = self.calc.divide(i, j)
            self.assertEqual(n, i / j)
        self.assertRaises(ZeroDivisionError, self.calc.divide, 11, 0)
        pass


    def test_sqrt(self):
        param_list = [12, 45, 96, 87, 25]
        for i in param_list:
            n = self.calc.sqrt(i)
            self.assertEqual(n, math.sqrt(i))
        self.assertRaises(ValueError, self.calc.sqrt , - 1)
        pass


    def test_exp(self):
        param_list = [12, 45, 96, 87, 25]
        for i in param_list:
            n = self.calc.exp(i)
            self.assertEqual(n, math.exp(i))
        self.assertRaises(TypeError, self.calc.exp, "1")
        pass


if __name__ == "__main__":
    unittest.main()

import unittest


class Calculations():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b
    
    def diff(self):
        return self.a - self.b
    

class TestCalculations(unittest.TestCase):
    def test_sum(self):
        calc = Calculations(8, 2)
        self.assertEqual(calc.sum(), 10, "The sum is wrong.")

    def test_diff(self):
        calc = Calculations(8, 2)
        self.assertEqual(calc.diff(), 6, "Error difference")

unittest.main()
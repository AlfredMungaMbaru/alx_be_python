import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        # Test basic addition
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0), 0)
        
        # Test with floating point numbers
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertEqual(self.calc.add(-2.5, 2.5), 0.0)
        
        # Test with large numbers
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)

    def test_subtraction(self):
        """Test the subtraction method."""
        # Test basic subtraction
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        
        # Test with floating point numbers
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
        self.assertEqual(self.calc.subtract(-2.5, -2.5), 0.0)
        
        # Test with negative results
        self.assertEqual(self.calc.subtract(3, 5), -2)

    def test_multiplication(self):
        """Test the multiplication method."""
        # Test basic multiplication
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        
        # Test with floating point numbers
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(-2.5, 4), -10.0)
        
        # Test with one
        self.assertEqual(self.calc.multiply(5, 1), 5)
        self.assertEqual(self.calc.multiply(1, 5), 5)

    def test_division(self):
        """Test the division method."""
        # Test basic division
        self.assertEqual(self.calc.divide(6, 2), 3.0)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-6, 2), -3.0)
        self.assertEqual(self.calc.divide(-6, -2), 3.0)
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        
        # Test with floating point numbers
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertEqual(self.calc.divide(-7.5, 2.5), -3.0)
        
        # Test division by one
        self.assertEqual(self.calc.divide(5, 1), 5.0)
        
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-5, 0))


if __name__ == '__main__':
    unittest.main()

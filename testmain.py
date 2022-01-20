import unittest
import main

class TestTwoNumbersOperations(unittest.TestCase):
    def test_twoNumbers_is_instance_of_twoNumbers(self):
        twoNumbers = main.TwoNumbersOperations(7.5, 8.6)
        self.assertIsInstance(twoNumbers, main.TwoNumbersOperations)

    def test_twoNumbers_is_not_null(self):
        twoNumbers = main.TwoNumbersOperations(7.5, 8.6)
        self.assertNotEqual(twoNumbers.b, 0, "The second number is different of zero")

if __name__ == "__main__":
    unittest.main()
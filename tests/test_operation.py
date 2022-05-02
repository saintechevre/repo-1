
import unittest

from addition import addition

target = __import__("addition.py")
addition = target.addition




class TestAddition(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(3,4)== 7, "Should be 7")


if __name__ == '__main__':
    unittest.main()

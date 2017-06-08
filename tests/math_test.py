import unittest
import python_cpp_example

class MainTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(python_cpp_example.add(1, 1), 2)

    def test_subtract(self):
        self.assertEqual(python_cpp_example.subtract(1, 1), 0)

if __name__ == '__main__':
    unittest.main()
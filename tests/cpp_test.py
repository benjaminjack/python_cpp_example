import unittest
import subprocess
import os


class MainTest(unittest.TestCase):
    def test_cpp(self):
        print("\n\nTesting C++ code...")
        subprocess.check_call(os.path.join(os.path.dirname(
            os.path.relpath(__file__)), 'bin', 'python_cpp_example_test'))
        print("\nResuming Python tests...\n")


if __name__ == '__main__':
    unittest.main()

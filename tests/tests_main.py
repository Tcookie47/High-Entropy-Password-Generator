import unittest
from src.main import return_strong_password, return_entropy

class TestPasswordGenerator(unittest.TestCase):
    def test_return_entropy(self):
        self.assertGreater(return_entropy("password"), 0)

    def test_return_strong_password(self):
        password = return_strong_password("test")
        self.assertGreater(len(password), 4)

if __name__ == "__main__":
    unittest.main()

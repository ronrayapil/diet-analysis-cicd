import unittest

class TestApp(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)
        print("test passed")

if __name__ == '__main__':
    unittest.main()

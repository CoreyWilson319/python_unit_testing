import unittest
import name 

class TestName(unittest.TestCase):
    def test_add(self):
        self.assertEqual(name.greater_than_5(10), True, 'Should return True')

if __name__ == '__main__':
    unittest.main()
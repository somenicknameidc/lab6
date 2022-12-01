import unittest
from main import calc

class calcTest(unittest.TestCase):
    def test_first(self):
        self.assertEqual(calc('1 2'), 3)
    
    def test_second(self):
        self.assertEqual(calc('3 4'), 7)
    
    def test_third(self):
        self.assertEqual(calc('100 200'), 300)
    
    def test_fourth(self):
        self.assertEqual(calc('-1 2'), 2)

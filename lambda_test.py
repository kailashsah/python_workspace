import unittest
from lambda_demo import get_cube

class Test1(unittest.TestCase):
    
    def testone(self):
        ret = get_cube(10)
        self.assertEqual(ret, 1000)
        
if __name__ == '__main__':
    unittest.main()
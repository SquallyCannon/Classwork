import unittest

class TestMain(unittest.TestCase):
    
    def test_location(self):
        a = 'red'
        b = 'red'
        self.assertEqual(a,b)

    #def test_truth(self):
        #self.assertTrue(2+ 5 *3 == 21)

if __name__ == '__main__':
    unittest.main()





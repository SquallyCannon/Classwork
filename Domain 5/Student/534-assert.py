import unittest

class TestMain(unittest.TestCase):
    
    def test_location(self):
        a = 'red'
        b = 'red'
        self.assertEqual(a,b)

    def test_truth(self):
        self.assertTrue((2 + 5) * 3 == 21)

    def test_is(self):
        a = 'red'
        b = 'red'
        self.assertIs(a,b)

    def test_in(self):
        a = 'red'
        b = ['red','green','blue']
        self.assertIn(a,b)

    #def test_is_instance(self):
        #city = City()
        #self.assertIsInstance(city, City)

if __name__ == '__main__':
    unittest.main()






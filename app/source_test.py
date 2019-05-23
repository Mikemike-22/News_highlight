import unittest
from models import source
Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    test class to test the behaviour of the source class
    '''

    def setUp(self):
        '''
        set up methpd that will run before every test
        '''
        self.new_source = Source('samsung','this is samsung','this is a review about samsung','https://www.samsung.com/us/')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
    unittest.main()

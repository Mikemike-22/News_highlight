import unittest
from models import article

Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test class to test behaviour of article class
    '''
    def setUp(self):
        '''
        setup method that will run before every test
        '''
        self.new_article = Article('mike','about ba','this is about ba','http://techcrunch.com/2019/05/15/binance-resumes-trading-following-40m-bitcoin-hack/','https://techcrunch.com/wp-content/uploads/2018/09/binance.jpg?w=600','2019-05-15T13:38:58Z')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

if __name__ == '__main__':
    unittest.main()

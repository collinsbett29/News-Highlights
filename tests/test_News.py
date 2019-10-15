import unittest
import app.models import News

class NewsTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run beforfe every Test
        '''
        self.new_News = News(1234,'Top Headlines of the Week','Terrorist Attack','/khsjha27hbs',8.5,129993) 

    def test_instance(self):
        self.assertTrue(isinstance(self.new_News,News))
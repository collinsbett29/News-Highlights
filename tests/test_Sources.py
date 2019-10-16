import unittest
from app.models import Sources,Articles

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('Daily Nation','Nation news','Kipchoge breaks his own record','dailynation.co.ke','general','Kenya','eng')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,'Daily Nation')
        self.assertEquals(self.new_source.name,'Nation news')
        self.assertEquals(self.new_source.description,'Kipchoge breaks his own record')
        self.assertEquals(self.new_source.url,'dailynation.co.ke')
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.country,'Kenya')
        self.assertEquals(self.new_source.language,'eng')

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('null','Kgothatso','Maimanes allies poke holes in coup report','Space engineer proposes accelerator propelling craft close to light speed - Express.co.uk','null.com','null.com/lg.jpg','2019-10-14T07:32:00Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'null')
        self.assertEquals(self.new_article.author,'Kgothatso')
        self.assertEquals(self.new_article.title,'Maimanes allies poke holes in coup report')
        self.assertEquals(self.new_article.description,'Space engineer proposes accelerator propelling craft close to light speed - Express.co.uk')
        self.assertEquals(self.new_article.url,'null.com')
        self.assertEquals(self.new_article.image,'null.com/null.jpg')
        self.assertEquals(self.new_article.date,'2019-10-14T07:32:00Z')
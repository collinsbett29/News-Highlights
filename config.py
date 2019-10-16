import os

class Config:
    '''
    General configuration parent class
    '''
    SOURCES_BASE_URL ='https://newsapi.org/v2/sources?apiKey={}'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?domains=wsj.com,nytimes.com&apiKey='
    NEWS_API_KEY ='0fb1cd6ef5614bfca5182c188b85f2b9'
    
    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
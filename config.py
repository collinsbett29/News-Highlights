import os

class Config:

    NEWS_API_URL = 'https://newsapi.org/v2/everything?q=bitcoin&from=2019-09-13&sortBy=publishedAt&apiKey={}'
    NEWS_API_KEY = os.environ.get(NEWS_API_KEY)

class prodConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':prodConfig
}    
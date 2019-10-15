class News:
    '''
    News class to define News objects
    '''

    def __init__(self,id,name,title,author,url,urlToImage,publishedAt):
        self.id = id
        self.name = name
        self.title = title
        self.author = author
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

class Article:
    all_articles = []

    def __init__(self,id,name,author,title,description,url,urlToImage,publishedAt,content):

        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

    def save_article(self):
        Articles.all_articles.append(self)

    @classmethod
    def clear_article(cls):
        Article.all_articles.clear()

    @classmethod
    def get_articles(cls,id):

        response = []

        for article in cls.all_articles:
            if article.news_id == id:
                response.append(article)

        return response                   

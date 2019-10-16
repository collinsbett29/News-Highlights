class Sources:
    '''
    Source class to define News objects
    '''

    def __init__(self,id,name,title,author,url,urlToImage,publishedAt):
        self.id = id
        self.name = name
        self.title = title
        self.author = author
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

class Articles:
    '''
    Article class to define article object
    '''
    def __init__(self,id,name,author,title,description,url,urlToImage,publishedAt,content):

        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

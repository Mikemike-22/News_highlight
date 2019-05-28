class Article:
    '''
    Articles class to define articles object
    '''

    def __init__(self,author,title,description,url,urlToImage,publishedAt):

        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt


class Source:
    '''
    Source class to define Source objects
    '''

    def __init__(self,id,name,description,url):

        self.id = id
        self.name = name
        self.description = description
        self.url = url

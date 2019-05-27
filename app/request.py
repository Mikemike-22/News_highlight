from app import app
import urllib.request,json
from .models import source,article

Source = source.Source
Article = article.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

# getting the news base url
base_url = app.config['NEWS_API_BASE_URL']

base_url_article= app.config['ARTICLES_API_BASE_URL']


def get_source(category):
    '''
    function that gets the json response to our url request
    '''
    get_source_url= base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)


    return source_results


def process_results(source_list):
    '''
    function that proceses the source results and transform them to a list of Objects
    '''
    source_results = []

    for source_item in source_list:

        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')

        source_object = Source(id,name,description,url)
        source_results.append(source_object)

    return source_results

def get_article(id):
    '''
    function that gets json response to url request
    '''
    get_article_url = base_url_article.format(id,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            article_results = process_article(get_article_response['articles'])

    return article_results

def process_article(article_list):
    '''
    function that processes news articles and returns them to a list of objects
    '''
    article_results = []

    for article_item in article_list:
        id = article_item.get('id')
        name = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if urlToImage:
            article_object = Articles(id,name,author,title,description,url,urlToImage,publishedAt,content)
            article_results.append(article_object)

    return articles_results

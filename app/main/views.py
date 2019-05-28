from flask import render_template,request
from . import main
from ..request import get_source,get_article


# views
@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''

    # getting news category
    business_news = get_source('business')
    # getting sports news
    sports_news = get_source('sports')
    # getting entertainment news
    entertainment_news = get_source('entertainment')
    # getting health news
    health_news = get_source('health')
    # getting science news
    science_news = get_source('science')
    # getting technology news
    technology_news = get_source('technology')

    title = "Home = Welcome to your source of News"
    return render_template('index.html', title = title, business = business_news, sports= sports_news, entertainment = entertainment_news, health = health_news, science = science_news, technology = technology_news)

@main.route('/article/<article_id>')
def article(article_id):
    '''
    view page function that returns the news details page and its data
    '''

    articles = get_article(id)
    # title = f'{article_id}'

    return render_template('article.html', id = id, articles = articles )

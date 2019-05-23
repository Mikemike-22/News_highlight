from flask import render_template
from app import app

# views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    title = "Home = Welcome to your source of News"
    return render_template('index.html', title = title)

@app.route('/article/<article_id>')
def article(article_id):
    '''
    view page fundtion that returns the news details page and its data
    '''
    title = f'You are viewing {article_id}'
    return render_template('article.html', title = title)

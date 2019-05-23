from flask import render_template
from app import app

# views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    message = "Hello world"
    return render_template('index.html', message = message)

@app.route('/article/<int:article_id>')
def article(article_id):
    '''
    view page fundtion that returns the news details page and its data
    '''
    return render_template('article.html', id = article_id)

    

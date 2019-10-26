from flask import  render_template,redirect,url_for,request
from . import main
from ..models import Sources
from ..requests import get_sources, get_articles


#Views
@main.route('/')
def index():
    
    '''
    
    View root page function that returns the index page and  its data
    
    '''
    sources = get_sources()
    print(sources)
    
    title = 'Home - Some of the best news sources'
    return render_template('index.html', title = title, sources = sources)

@main.route('/news')
def news():
    
    '''
    Views the news page functionality that returns newshighlights details and its data
    
    '''
    articles = get_articles()
    title = 'Articles - Some of the articles'
    return render_template('news.html', articles=articles, title = title)
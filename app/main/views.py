from flask import render_template,request,redirect,url_for
from . import main
from ..models import Sources
from ..requests import get_sources, get_articles

# views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and  its data
    '''
    sources = get_sources()
    print(sources)
    
    title = 'Sources - Some of the best news sources'
    return render_template('index.html', title = title, sources = sources)

@main.route('/news')
def news():
    '''
    Views the news page functionality that returns news highlights
    '''
    articles = get_articles()
    title = 'Articles - Some of the articles'
    return render_template('news.html', articles=articles, title = title)
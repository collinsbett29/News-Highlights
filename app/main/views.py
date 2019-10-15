from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_news,search_news
from .forms import ReviewForm
from ..models import Review

# views
@main.route('/')
def index():
    '''
    View root page function that returns index page and its data
    '''
    # Getting news sources
    business_news = get_news('business')
    entertainment_news = get_news('entertainment')
    health_news = get_news('health')
    science_news = get_news('science')
    sports_news = get_news('sports')
    technology_news = get_news('technology')
    
    title = 'Home - Welcome to the Updated News Website'
    return render_template('index.html',business = business_news,entertainment = entertainment_news,health = health_news,science = science_news,sports = sports_news,technology = technology_news)

@main.route('/news/<int:id>')
def news(id):
    '''
    View news page function that returns the news details page and its data 
    '''
    news = get_news(id)
    title = f'{news.title}'
    description = Description.get_news(news.id)

    return render_template('news.html',title = title,news = news,description = description)   


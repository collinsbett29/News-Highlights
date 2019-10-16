# News Highlight

## Author
   Collins K. Bett

## Description
This is a Python client library for News API V2. The functions and methods for this library should mirror the endpoints specified by the News API documentation.

## Installation
Installation for the package can be done via pip:

             $ python -m pip install News-Highlights
### Usage
After installation, import the client class into your project:

              from newsapi import NewsApiClient 

Initialize the client with your API key:

               api = NewsApiClient(api_key='XXXXXXXXXXXXXXXXXXXXXXX')

### Technologies Used
* Python 3.6
* Flask Framework
* HTML/CSS
* JavaScript              

### Top Headlines
Use .get_top_headlines() to pull from the /top-headlines endpoint:

api.get_top_headlines(sources='bbc-news')
Everything
Use .get_everything() to pull from the /everything endpoint:

api.get_everything(q='bitcoin')
### Sources
Use .get_sources() to pull from the /sources endpoint:

### api.get_sources()
For Windows users printing to cmd or powershell
You will encounter an error if you attempt to print the .json() object to the command line. This is because the '{', '}' curly braces to be printed to the console. This becomes especially annoying if developers wish to get 'under the hood'.

### Support
Feel free to make suggestions or provide feedback. 
Thanks. 
Reach out at collinsbett29@gmail.com

### License
This application is licensed under MIT license

                      © Collins K. Bett 2019 
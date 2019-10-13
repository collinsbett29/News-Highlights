# General
This is a Python client library for News API V2. The functions and methods for this library should mirror the endpoints specified by the News API documentation.

## Installation
Installation for the package can be done via pip:

$ python -m pip install newsapi-python
Usage
After installation, import the client class into your project:

from newsapi import NewsApiClient
Initialize the client with your API key:

api = NewsApiClient(api_key='XXXXXXXXXXXXXXXXXXXXXXX')
Endpoints
An instance of NewsApiClient has three instance methods corresponding to three News API endpoints.

Top Headlines
Use .get_top_headlines() to pull from the /top-headlines endpoint:

api.get_top_headlines(sources='bbc-news')
Everything
Use .get_everything() to pull from the /everything endpoint:

api.get_everything(q='bitcoin')
Sources
Use .get_sources() to pull from the /sources endpoint:

api.get_sources()
For Windows users printing to cmd or powershell
You will encounter an error if you attempt to print the .json() object to the command line. This is because the '{', '}' curly braces to be printed to the console. This becomes especially annoying if developers wish to get 'under the hood'.

Here is the error:

UnicodeEncodeError: 'charmap' codec can't encode character '\u2019' in position 1444: character maps to <undefined>
This can be fixed by: - installing 'win-unicode-console' py -mpip install win-unicode-console - then running it while calling your python script... py -mrun myPythonScript.py

Another option is hardcoding your console to only print in utf-8. This is a bad idea, as it could ruin many other scripts and/or make errors MUCH more difficult to track. More information.

Support
Feel free to make suggestions or provide feedback regarding the library. Thanks. Reach out at lisivickmatt@gmail.com
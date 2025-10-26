#A minimal application

''' An instance of this class will be our WSGI application. '''
from flask import Flask 

''' The first argument is the name of the application's module or package. __name__ is a convenient shortcut for this that is appropriate for most cases. 
    This is needed so that Flask knows where to look for resources such as templates and static files.
'''
app = Flask(__name__) 

'''
    The route() decorator in Flask is used to bind a function to a URL. 
    In this case, we are binding the hello_world function to the root URL ('/'). 
    When a user visits this URL, the hello_world function will be executed, and its return value will be sent to the user's web browser.
'''

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'
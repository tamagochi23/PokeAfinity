
from flask import Flask, request 
from markupsafe import escape


app = Flask(__name__) 

@app.route('/')
def index():
    return '<p>Welcome to the PokAfindsdity App!</p>'

@app.route('/hello')
def hello():
    name = request.args.get("name", "Flask")
    return f'<p>Hello00, {escape(name)}!!!</p>'

@app.route('/user/<username>') # dynamic route
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>') # specify that post_id is an integer
def show_post(post_id):
    # show the post with the given post_id
    return f'Post {escape(post_id)}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
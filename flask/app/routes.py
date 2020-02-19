from flask import render_template
from app import app

@app.route('/')         # decorators, a unique feature of the Python language.
@app.route('/index')    # A common pattern with decorators is to use them to register functions as callbacks for certain events.
def index():
    user = {'username': 'John'}

    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html', title="Matumaini", user=user, posts=posts)

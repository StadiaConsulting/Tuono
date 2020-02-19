from app import app

@app.route('/')         # decorators, a unique feature of the Python language.
@app.route('/index')    # A common pattern with decorators is to use them to register functions as callbacks for certain events.
def index():
    return "Hello, World!"

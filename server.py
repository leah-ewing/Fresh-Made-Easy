from flask import (Flask,render_template, request, flash, session,
                   redirect)
#from model import connect_to_db
#import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """Display the homepage."""

    return render_template('homepage.html')

@app.route('/login')
def login_page():
    """Display user login page."""

    return render_template('login.html')

@app.route('/sign-up')
def sign_up_page():
    """Display user sign-up page."""

    return render_template('sign-up.html')

#add your /user-profile.html app route


#put your app routes here! :D


if __name__ == '__main__':
    #connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
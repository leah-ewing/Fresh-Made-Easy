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
def loginPage():
    """Display user login page."""

    return render_template('login.html')

@app.route('/sign-up')
def signUpPage():
    """Display user sign-up page."""

    return render_template('sign-up.html')

@app.route('/user-profile')
def userProfile():
    """Display user's profile page."""

    return render_template('user-profile.html')

@app.route('/about-us')
def aboutUsPage():
    """Dispay Fresh Made Easy's 'About Us' page"""

    return render_template('about-us.html')


#put your app routes here! :D


if __name__ == '__main__':
    #connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
from flask import (Flask,render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud
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


@app.route('/', methods = ["POST"])
def loginUser():
    """Login user and redirect to homepage."""

    email = request.form.get("email")
    password = request.form.get("password")

    valid_user = crud.login_user(email, password)

    if valid_user:
        flash("Welcome back!")
    else:
        flash("Invalid login. Please try again.")
        return redirect("/login") 
    
    return render_template("homepage.html")


@app.route('/user-profile', methods = ["POST"])
def createUser():
    """Create a new user and redirect them to their profile."""

    email = request.form.get("email")
    password = request.form.get("password")
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    username = request.form.get("username")

    user_email = crud.get_user_by_email(email)
    user_username = crud.get_user_by_username(username)

    if user_email:
        flash("Profile already exists with that email. Please login.")
        return redirect("/login")
    elif user_username:
        flash("Username not available, please try again.")
        return redirect("/sign-up")
    else:
        crud.create_user(email, password, fname, lname, username)
        
    return render_template('user-profile.html')


@app.route('/about-us')
def aboutUsPage():
    """Display Fresh Made Easy's 'About Us' page"""

    return render_template('about-us.html')



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
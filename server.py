from flask import (Flask,render_template, request, flash, session,
                   redirect)
from model import User, connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """Display the homepage."""

    return render_template('homepage.html')


@app.route('/')
def index():
    if "email" in session:
        fname = session['email']
        return fname + ", you have been logged in."


@app.route('/', methods = ["POST"])
def loginUser():
    """Login user and redirect them to the homepage"""

    email = request.form.get("email")
    password = request.form.get("password")
    #fname = request.form.get("fname")

    valid_user = crud.login_user(email, password)

    if valid_user:
        session["email"] = True
        flash(f"Welcome back, {email}!")
    else:
        flash("Invalid login. Please try again.")
        return redirect("/login") 
    
    return render_template("homepage.html")
# ***   ^ I want this to eventually say the user's first name, not their email ***

@app.route('/logout')
def logout():
    """Logout user."""

    session.pop('email', None)
    flash("You have been signed out!")
    return redirect('/')

    return render_template("homepage.html")


@app.route('/login')
def loginPage():
    """Display user login page."""

    return render_template('login.html')


@app.route('/sign-up')
def signUpPage():
    """Display user sign-up page."""

    return render_template('sign-up.html')


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
        flash("Account created! Please login.")
        
    return render_template('login.html')


@app.route('/about-us')
def aboutUsPage():
    """Display Fresh Made Easy's 'About Us' page."""

    return render_template('about-us.html')


@app.route('/shopping-cart')
def shoppingCart():
    """Display a user's shopping cart."""

    return render_template('shopping-cart.html')



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
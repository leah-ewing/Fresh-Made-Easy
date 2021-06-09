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


@app.route('/', methods = ["POST"])
def loginUser():
    """Login user and redirect them to the homepage."""

    email = request.form.get("email")
    password = request.form.get("password")

    fname = crud.get_user_fname(email)
    valid_user = crud.login_user(email, password)

    if valid_user:
        session["current_user"] = email
        flash(f"Welcome back, {fname}!")
    else:
        flash("Invalid login. Please try again.")
        return redirect("/login") 
    
    return render_template("homepage.html")


@app.route('/logout')
def logout():
    """Logout user."""

    if session["current_user"]:
        session["current_user"] = False
        session.pop('email', None)
        flash("You have been signed out!")
        return redirect('/')
    else:
        flash("Please login.")
        return redirect('/')

    return render_template("homepage.html")


@app.route('/login')
def loginPage():
    """Display user login page."""

    if session["current_user"]:
        return redirect('/')
    else:
        return render_template('login.html')


@app.route('/sign-up')
def signUpPage():
    """Display user sign-up page."""

    if session["current_user"]:
        return redirect('/')
    else:
        return render_template('sign-up.html')


@app.route('/user-profile', methods = ["POST"])
def createUser():
    """Create a new user and redirect them to their profile."""

    email = request.form.get("email")
    password = request.form.get("password")
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    username = request.form.get("username")

    user_username = crud.user_username(username)
    user_email = crud.get_user_by_email(email)
    
    if user_username:
        flash("Username not available, please try again.")
        return redirect("/sign-up")
    elif user_email:
        flash("Profile already exists with that email. Please login.")
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

    if session["current_user"]:
        return render_template('shopping-cart.html')
    else:
        flash("Please login.")
        return redirect('/')


@app.route('/user-profile')
def userProfile():
    """Display a user's profile page."""

    email = session["current_user"]
    fname = crud.get_user_fname(email)
    lname = crud.get_user_lname(email)
    username = crud.get_user_by_username(email)

    if session["current_user"]:
        return render_template('user-profile.html',
                                fname = fname,
                                lname = lname,
                                username = username,
                                email = email)
    else:
        flash("Please login.")
        return redirect('/')


@app.route('/all-pickup-locations')
def allPickupLocations():
    """Displays all pickup locations."""

    return render_template('all-pickup-locations.html')


@app.route('/all-farms')
def allFarms():
    """Displays all farms."""

    return render_template('all-farms.html')


@app.route('/shop')
def shop():
    """Takes user to the shop page."""

    return render_template('shop.html')


@app.route('/how-it-works')
def howItWorks():
    """Displays 'How It Works' page."""

    return render_template('how-it-works.html')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
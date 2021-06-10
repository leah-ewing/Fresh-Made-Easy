from flask import (Flask,render_template, request, flash, session,
                   redirect)
from model import User, connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined





# @app.route('/')
# def homepage():
#     """Display the homepage."""

#     return render_template('homepage.html')


@app.route('/')
def index():
    """Create user session"""

    if "current_user" in session:
        current_user = session["current_user"]
  
        return render_template('homepage.html', current_user = current_user)
    else:
       return render_template('homepage.html', current_user = None)


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
        return render_template("homepage.html", current_user = session["current_user"])
    else:
        flash("Invalid login. Please try again.")
        return redirect("/login", current_user = None) 
    

@app.route('/logout')
def logout():
    """Logout user."""

    if "current user" in session:
        session["current_user"] = False
        session.pop('email', None)
        flash("You have been signed out!")
        return redirect('/')
    else:
        flash("Please login.")
        return redirect('/', current_user = None)

    #return render_template("homepage.html", current_user = None)


@app.route('/login')
def loginPage():
    """Display user login page."""

    if "current_user" in session:
        return redirect('/')
    else:
        return render_template('login.html', current_user = None)


@app.route('/sign-up')
def signUpPage():
    """Display user sign-up page."""

    if "current_user" in session:
        return redirect('/')
    else:
        return render_template('sign-up.html', current_user = None)


@app.route('/user-profile', methods = ["POST"])
def createUser():
    """Create a new user and redirect them to login page."""

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
    elif len(fname) > 25:
        flash("Please limit first name to 25 characters.")
        return redirect("/sign-up")
    elif len(lname) > 25:
        flash("Please limit last name to 25 characters.")
        return redirect("/sign-up")
    elif len(username) > 25:
        flash("Please limit username to 25 characters.")
        return redirect("/sign-up")
    else:
        crud.create_user(email, password, fname, lname, username)
        flash("Account created! Please login.")
        
    return render_template('login.html', current_user = session['current_user'])


@app.route('/about-us')
def aboutUsPage():
    """Display Fresh Made Easy's 'About Us' page."""

    return render_template('about-us.html', current_user = session['current_user'])


@app.route('/shopping-cart')
def shoppingCart():
    """Display a user's shopping cart."""

    if "current_user" in session:
        return render_template('shopping-cart.html', current_user = session['current_user'])
    else:
        flash("Please login.")
        return redirect('/', current_user = None)


@app.route('/user-profile')
def userProfile():
    """Display a user's profile page."""

    email = session["current_user"]
    fname = crud.get_user_fname(email)
    lname = crud.get_user_lname(email)
    username = crud.get_user_by_username(email)

    if "current_user" in session:
        return render_template('user-profile.html',
                                fname = fname,
                                lname = lname,
                                username = username,
                                email = email,
                                current_user = session['current_user'])
    else:
        flash("Please login.")
        return redirect('/', current_user = None)


@app.route('/all-pickup-locations')
def allPickupLocations():
    """Displays all pickup locations."""


    return render_template('all-pickup-locations.html', current_user = session['current_user'])


@app.route('/all-farms')
def allFarms():
    """Displays all farms."""

    return render_template('all-farms.html', current_user = session['current_user'])


@app.route('/shop')
def shop():
    """Takes user to the shop page."""

    return render_template('shop.html', current_user = session['current_user'])


@app.route('/how-it-works')
def howItWorks():
    """Displays 'How It Works' page."""

    return render_template('how-it-works.html', current_user = session['current_user'])


@app.route('/pickup-location-info')
def pickupLocationInfo():
    """Displays information for a pickup location."""

    return render_template('pickup-location-info.html', current_user = session['current_user'])


@app.route('/farm-info')
def farmInfo():
    """Displays information for a farm."""

    return render_template('farm-info.html', current_user = session['current_user'])


@app.route('/user-purchases')
def userPurchases():
    """Displays user's purchase history."""

    fname = crud.get_user_fname(session['current_user'])

    return render_template('user-purchases.html', fname = fname, current_user = session['current_user'])


@app.route('/item-info')
def itemInfo():
    # ^ 'item' argument here?
    """Displays information for an item."""

    # item = session['current_item']

    # item_name = crud.get_item_name(item)
    # item_description = crud.get_item_description(item)
    # item_cost = crud.get_item_cost(item)

    return render_template('item-info.html/', current_user = session['current_user']
                            # ,item_name = item_name,
                            # item_description = item_descriptiom,
                            # item_cost = item_cost
                            )
    #session for current item isn't working


@app.route('/checkout')
def checkout():
    """Displays checkout page."""

    if "current_user" in session:
        return render_template('checkout.html', current_user = session['current_user'])
    else:
        flash("Please login.")
        return redirect('/', current_user = None)


@app.route('/confirmed')
def confirmed():
    """Displays a confirmation of a purchase."""

    if "current_user" in session:
        return render_template('confirmed.html', current_user = session['current_user'])
    else:
        flash("Please login.")
        return redirect('/', current_user = None)    


@app.route('/purchase-info')
def purchaseInfo():
    """Displays information for a user's purchase."""

    if "current_user" in session:
        return render_template('purchase-info.html', current_user = session['current_user'])
    else:
        flash("Please login.")
        return redirect('/', current_user = None)  


@app.route('/add-item-to-cart')
def addItemToCart():
    """Adds an item to the user's shopping cart."""

    return render_template('shopping-cart.html', current_user = session['current_user'])
    #temporary route




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
from flask import (Flask,render_template, request, flash, session,
                   redirect)
from model import User, connect_to_db
import crud, requests, json
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined





# @app.route('/')
# def homepage():
#     """Display the homepage."""

#     return render_template('homepage.html')


@app.route('/')
def homepage():
    """Display the homepage"""

    if session["current_user"]:
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
        return redirect("/login") 
    

@app.route('/logout')
def logout():
    """Logout user."""

    if session["current_user"]:
        session["current_user"] = False
        session.pop("email", None)
        flash("You have been signed out!")
        return redirect('/')
    else:
        flash("Please login.")
        return redirect('/')


@app.route('/login')
def loginPage():
    """Display user login page."""

    if session["current_user"]:
        return redirect('/')
    else:
        return render_template('login.html', current_user = None)


@app.route('/sign-up')
def signUpPage():
    """Display user sign-up page."""

    if session["current_user"]:
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

    if session["current_user"]:
        return render_template('about-us.html', current_user = session['current_user'])
    else:
        return render_template('about-us.html', current_user = None)


@app.route('/shopping-cart')
def shoppingCart():
    """Display a user's shopping cart."""

    if session["current_user"]:
        return render_template('shopping-cart.html', current_user = session['current_user'])
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
                                email = email,
                                current_user = session['current_user'])
    else:
        flash("Please login.")
        return redirect('/')


@app.route('/all-pickup-locations')
def allPickupLocations():
    """Displays all pickup locations."""

    if session["current_user"]:
        return render_template('all-pickup-locations.html', current_user = session['current_user'])
    else:
        return render_template('all-pickup-locations.html', current_user = None)


@app.route('/all-farms')
def allFarms():
    """Displays all farms."""

    if session["current_user"]:
        return render_template('all-farms.html', current_user = session['current_user'])
    else:
        return render_template('all-farms.html', current_user = None)


@app.route('/shop')
def shop():
    """Takes user to the shop page."""

    if session["current_user"]:
        return render_template('shop.html', current_user = session['current_user'])
    else:
        flash("Please login to view items!")
        return render_template('homepage.html', current_user = None)
    

@app.route('/how-it-works')
def howItWorks():
    """Displays 'How It Works' page."""

    if session['current_user']:
        return render_template('how-it-works.html', current_user = session['current_user'])
    else:
        return render_template('how-it-works.html', current_user = None)


@app.route('/pickup-location-info')
def pickupLocationInfo():
    """Displays information for a pickup location."""

    if session["current_user"]:
        return render_template('pickup-location-info.html', current_user = session['current_user'])
    else:
        return render_template('pickup-location-info.html', current_user = None)
    

@app.route('/farm-info')
def farmInfo():
    """Displays information for a farm."""
    
    if session["current_user"]:
        return render_template('farm-info.html', current_user = session['current_user'])
    else: 
        return render_template('farm-info.html', current_user = None)


@app.route('/user-purchases')
def userPurchases():
    """Displays user's purchase history."""

    fname = crud.get_user_fname(session['current_user'])

    if session["current_user"]:
        return render_template('user-purchases.html', fname = fname, current_user = session['current_user'])
    else:
        flash("Please login.")
        return render_template('homepage.html', current_user = None)


#*****
@app.route('/item-info', methods = ["GET"])
                                #    ^ because I'm GETting information?
def itemInfo():
    # ^ 'item' argument here? item id?
    """Displays information for an item."""

    current_item = request.form.get("items")
    # taking the link to 'item-info' and setting it as a variable 'current_item'

    if session['current_user']:
        session['current_item'] = True
        # creates a session attached to the current_item link that was clicked...maybe...?
        items = json.loads(open("static/items.json", "r").read())
        # opens items.json and converts it to a dictionary
        for item in items:
        # iterates through each item in items.json
            item_name = item.item_name
            # sets the variable item_name to an individual item's name
            item_description = item.item_description
            # sets the variable item_description to an individual item's description
            item_cost = item.item_cost
            # sets the variable item_cost to an individual item's description
            return render_template('item-info.html', 
                                    current_user = session["current_user"],
                                    item_name = item_name,
                                    item_description = item_description,
                                    item_cost = item_cost)
        else:
            flash("Please login.")
            return render_template('homepage.html', current_user = None)
# page not currently loading: AttributeError: 'dict' object has no attribute 'item_name'
# line 247 - item_name = item.item_name
# when I test 'items' in interactive mode, everything looks good with the dictionary
# tried reformatting json file (items-2.json), get the same error but with 'str':
# ^ AttributeError: 'str' object has no attribute 'item_name'


@app.route('/checkout')
def checkout():
    """Displays checkout page."""

    if session["current_user"]:
        return render_template('checkout.html', current_user = session['current_user'])
    else:
        flash("Please login.")
        return render_template('homepage.html', current_user = None)


@app.route('/confirmed')
def confirmed():
    """Displays a confirmation of a purchase."""

    if session["current_user"]:
        return render_template('confirmed.html', current_user = session['current_user'])
    else:
        flash("Please login.")
        return render_template('homepage.html', current_user = None)    


@app.route('/purchase-info')
def purchaseInfo():
    """Displays information for a user's purchase."""

    if session["current_user"]:
        return render_template('purchase-info.html', current_user = session['current_user'])
    else:
        flash("Please login.")
        return render_template('homepage.html', current_user = None)  


@app.route('/add-item-to-cart')
def addItemToCart():
    """Adds an item to the user's shopping cart."""

    if session["current_user"]:
        return render_template('shopping-cart.html', current_user = session['current_user'])
    else:
        flash("Please login.")
        return render_template('homepage.html', current_user = None)
    #temporary route




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
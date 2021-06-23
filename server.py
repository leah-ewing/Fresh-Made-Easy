from flask import (Flask,render_template, request, flash, session, redirect)
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

    if "current_user" in session:
        current_user = session["current_user"]
        return render_template('homepage.html', current_user = "current_user")
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
        session["shopping_cart"] = []
        session["total"] = 0
        flash(f"Welcome back, {fname}!")
        return render_template("homepage.html", current_user = "current_user")
    else:
        flash("Invalid login. Please try again.")
        return render_template('login.html', current_user = None)
    

@app.route('/logout')
def logout():
    """Logout user."""

    if "current_user" in session:
        session["current_user"] = None
        session.pop("email", None)
        flash("You have been signed out!")
        return redirect("/")
    else:
        flash("Please login.")
        return render_template("homepage.html", current_user = None)


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
        return redirect("/")
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
        
    return render_template('login.html', current_user = "current_user")


@app.route('/about-us')
def aboutUsPage():
    """Display Fresh Made Easy's 'About Us' page."""

    if "current_user" in session:
        return render_template('about-us.html', current_user = "current_user")
    else:
        return render_template('about-us.html', current_user = None)


@app.route('/shopping-cart')
def shoppingCart():
    """Display a user's shopping cart."""

    if "current_user" in session:
        return render_template('shopping-cart.html', 
                                current_user = "current_user", 
                                shopping_cart = session["shopping_cart"],
                                total = session["total"])
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

    if "current_user" in session:
        return render_template('user-profile.html',
                                fname = fname,
                                lname = lname,
                                username = username,
                                email = email,
                                current_user = "current_user")
    else:
        flash("Please login.")
        return redirect('/')


@app.route('/all-pickup-locations')
def allPickupLocations():
    """Displays all pickup locations."""

    if "current_user" in session:
        return render_template('all-pickup-locations.html', current_user = "current_user")
    else:
        return render_template('all-pickup-locations.html', current_user = None)


@app.route('/all-farms')
def allFarms():
    """Displays all farms."""

    if "current_user" in session:
        return render_template('all-farms.html', current_user = "current_user")
    else:
        return render_template('all-farms.html', current_user = None)


@app.route('/shop')
def shop():
    """Takes the user to the shop page."""

    if "current_user" in session:
        return render_template('shop.html', current_user = "current_user")
    else:
        flash("Please login to shop!")
        return render_template('homepage.html', current_user = None)


@app.route('/all-items')
def allItems():
    """Shows a user all items available for purchase."""

    if "current_user" in session:
        return render_template('all-items.html', current_user = "current_user")
    else:
        flash("Please login to view items!")
        return render_template('homepage.html', current_user = None)
    

@app.route('/how-it-works')
def howItWorks():
    """Displays 'How It Works' page."""

    if "current_user" in session:
        return render_template('how-it-works.html', current_user = "current_user")
    else:
        return render_template('how-it-works.html', current_user = None)


@app.route('/pickup-location-info/<current_location>', methods = ["GET"])
def pickupLocationInfo(current_location):
    """Displays information for a pickup location."""
    location = crud.get_pickup_location_by_name(current_location)

    if "current_user" in session and location != None:
        return render_template('pickup-location-info.html', 
                                current_user = "current_user",
                                location_name = location.location_name,
                                location_address = location.location_address,
                                neighborhood_name = location.neighborhood_name)
    else:
        return render_template('pickup-location-info.html', 
                                current_user = None,
                                location_name = location.location_name,
                                location_address = location.location_address,
                                neighborhood_name = location.neighborhood_name)


@app.route('/farm-info/<current_farm>', methods = ["GET"])
def farmInfo(current_farm):
    """Displays information for a farm."""

    farm = crud.get_farm_by_name(current_farm)
    

    if 'current_user' in session and farm != None:
        return render_template('farm-info.html', 
                                    current_user = "current_user",
                                    farm_name = farm.farm_name,
                                    farm_address = farm.farm_address,
                                    farm_description = farm.farm_description)
    else:
        return render_template('farm-info.html', 
                                current_user = None, 
                                farm_name = farm.farm_name,
                                farm_address = farm.farm_address)


@app.route('/item-info/<current_item>', methods = ["GET"])
def itemInfo(current_item):
    """Displays information for an item."""
    
    item = crud.get_item_by_name(current_item)

    if 'current_user' in session and item != None:
        return render_template('item-info.html', 
                                    current_user = "current_user",
                                    item_name = item.item_name,
                                    item_description = item.item_description,
                                    item_cost = item.item_cost,
                                    item_img = item.item_img,
                                    farm_name = item.farm_name)
    else:
        flash("Please login.")
        return render_template('homepage.html', current_user = None)


@app.route('/user-purchases')
def userPurchases():
    """Displays user's purchase history."""

    email = session["current_user"]
    fname = crud.get_user_fname(email)
    user_id = crud.get_user_id_by_email(email)
    user_purchases = crud.get_all_purchases(user_id)
    

    if "current_user" in session:
        return render_template('user-purchases.html', fname = fname, current_user = "current_user", user_purchases = user_purchases)
    else:
        flash("Please login.")
        return render_template('homepage.html', current_user = None)


@app.route('/checkout')
def checkout():
    """Displays checkout page."""

    if "current_user" in session:
        if session['total'] == 0:
            flash("Add some items to your cart to checkout!")
            return redirect('/shopping-cart')
        if session['total'] > 0:
            return render_template('checkout.html', current_user = "current_user")
    else:
        flash("Please login.")
        return render_template('homepage.html', current_user = None)


@app.route('/confirmed')
def confirmed():
    """Displays a confirmation of a purchase."""
    user_id = crud.get_user_id_by_email(session["current_user"])
    items = str(session["shopping_cart"])
    date_time_of_purchase = "*"
    payment_method = request.form.get("payment_method")
    pickup_date = "*"
    pickup_location = request.form.get("location")
    purchase_total = session["total"]

    if "current_user" in session:
        crud.create_new_purchase(user_id, items, date_time_of_purchase, payment_method, pickup_date, pickup_location, purchase_total)
        session["shopping_cart"] = []
        session["total"] = 0
        return render_template('confirmed.html', current_user = "current_user")
    else:
        flash("Please login.")
        return render_template('homepage.html', current_user = None)    


@app.route('/purchase-info')
def purchaseInfo():
    """Displays information for a user's purchase."""

    if "current_user" in session:
        return render_template('purchase-info.html', current_user = "current_user")
    else:
        flash("Please login.")
        return render_template('homepage.html', current_user = None)  


@app.route('/add-item-to-cart/<current_item>', methods = ["POST"])
def addToCart(current_item):
    """Adds an item to the user's shopping cart."""
    item = crud.get_item_by_name(current_item)
    item_amount = request.form.get("add-to-cart")

    if "current_user" in session and item != None:
        if item.item_name == current_item:
            session["shopping_cart"].append([item.item_name, (int(item.item_cost) * int(item_amount)), item_amount])
            session["total"] += (int(item.item_cost) * int(item_amount))
            flash("Item added to cart!")
            return render_template('shopping-cart.html', 
                                    current_user = "current_user",
                                    shopping_cart = session["shopping_cart"],
                                    total = session["total"])
    elif "current_user" not in session:
        flash("Please login.")
        return render_template('homepage.html', current_user = None) 


# @app.route('/category-info/<current_category>', methods = ["GET"])
# def categoryInfo(current_category):
#     """Displays items fitting a category."""
    
#     item = crud.get_item_by_name(current_item)

#     if 'current_user' in session and item != None:
#         return render_template('item-info.html', 
#                                     current_user = "current_user",
#                                     item_name = item.item_name,
#                                     item_description = item.item_description,
#                                     item_cost = item.item_cost,
#                                     item_img = item.item_img,
#                                     farm_name = item.farm_name)
#     else:
#         flash("Please login.")
#         return render_template('homepage.html', current_user = None)

@app.route("/category-info/<current_category>", methods = ["GET"])
def categoryInfo(current_category):
    """Displays items fitting a category."""

    category = crud.get_category_by_name(current_category)

    if "current_user" in session and category != None:
        return render_template('category-info.html', 
                                current_user = "current_user",
                                category_name = category.category_name)
    else:
        flash("Please login.")
        return render_template('homepage.html', current_user = None)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
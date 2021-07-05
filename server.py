from flask import (Flask,render_template, request, flash, session, redirect)
from model import User, connect_to_db
import crud, requests, json
from jinja2 import StrictUndefined
from datetime import datetime

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined






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
        # return render_template("homepage.html", current_user = None)
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
    email = session["current_user"]
    user_id = crud.get_user_id_by_email(email)
    cart_ids = crud.get_cart_id_by_user_id(user_id)
    item_names = crud.get_item_names_in_cart(user_id)
    cart_total = crud.get_cart_total(user_id)
    fname = crud.get_user_fname(email)

    if "current_user" in session:
        return render_template('shopping-cart.html', 
                                current_user = "current_user",
                                cart_total = cart_total, 
                                cart_ids = cart_ids,
                                item_names = item_names,
                                fname = fname)
    else:
        flash("Please login.")
        return redirect('/')


@app.route('/user-profile')
def userProfile():
    """Display a user's profile page."""

    if "current_user" in session:
        email = session["current_user"]
        fname = crud.get_user_fname(email)
        lname = crud.get_user_lname(email)
        username = crud.get_user_by_username(email)
        return render_template('user-profile.html',
                                fname = fname,
                                lname = lname,
                                username = username,
                                email = email,
                                current_user = "current_user")
    else:
        flash("Please login.")
        return render_template('homepage.html', current_user = None)


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
    farm_items = crud.get_item_names_by_farm_name(current_farm)

    if 'current_user' in session and farm != None:
        return render_template('farm-info.html', 
                                    current_user = "current_user",
                                    farm_name = farm.farm_name,
                                    farm_address = farm.farm_address,
                                    farm_description = farm.farm_description,
                                    farm_items = farm_items)
    else:
        return render_template('farm-info.html', 
                                current_user = None, 
                                farm_name = farm.farm_name,
                                farm_address = farm.farm_address,
                                farm_description = farm.farm_description)


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
    purchases = crud.get_all_user_purchases(user_id)

    if "current_user" in session:
            return render_template('user-purchases.html', fname = fname, current_user = "current_user", purchases = purchases)
    else:
        flash("Please login.")
        return render_template('homepage.html', current_user = None)


@app.route('/checkout')
def checkout():
    """Displays checkout page."""

    email = session["current_user"]
    user_id = crud.get_user_id_by_email(email)
    cart_total = crud.get_cart_total(user_id)

    if "current_user" in session:
        if cart_total == 0:
            flash("Add some items to your cart to checkout!")
            return redirect('/shopping-cart')
        if cart_total > 0:
            return render_template('checkout.html', current_user = "current_user")
    else:
        flash("Please login.")
        return render_template('homepage.html', current_user = None)


@app.route('/confirmed', methods = ['POST'])
def confirmed():
    """Displays a confirmation of a purchase."""

    email = session["current_user"]
    user_id = crud.get_user_id_by_email(email)
    payment_method = request.form.get("payment-method")
    pickup_location = request.form.get("location")
    purchase_total = crud.get_cart_total(user_id)
    fname = crud.get_user_fname(email)
    purchase_placed = datetime.now()
    pickup_date = request.form.get("pickup-date")
    date_time_of_purchase = purchase_placed.strftime("%Y-%m-%d")
    
    if "current_user" in session:
        crud.create_new_purchase(user_id, date_time_of_purchase, payment_method, pickup_date, pickup_location, purchase_total)
        crud.delete_all_cart_items(user_id)
        return render_template('confirmed.html', current_user = "current_user", fname = fname)
    else:
        flash("Please login.")
        return render_template('homepage.html', current_user = None)  


@app.route('/purchase-info/<current_purchase>', methods = ["GET"])
def purchaseInfo(current_purchase):
    """Displays information for a user's purchase."""

    email = session["current_user"]
    fname = crud.get_user_fname(email)

    purchase_id = crud.get_current_purchase(current_purchase)
    purchase = crud.get_purchase_by_id(purchase_id)
    items = crud.get_items_in_purchase(purchase.purchase_id)

    if "current_user" in session:
        return render_template('purchase-info.html', 
                                current_user = "current_user", 
                                fname = fname,
                                purchase_id = purchase.purchase_id,
                                date_time_of_purchase = purchase.date_time_of_purchase,
                                pickup_location = purchase.pickup_location,
                                pickup_date = purchase.pickup_date,
                                payment_method = purchase.payment_method,
                                purchase_total = purchase.purchase_total,
                                items = items)
    else:
        flash("Please login.")
        return render_template('homepage.html', current_user = None) 


@app.route('/add-item-to-cart/<current_item>', methods = ["POST"])
def addToCart(current_item):
    """Adds an item to the user's shopping cart."""

    email = session["current_user"]
    item_id = crud.get_item_id_by_name(current_item)
    user_id = crud.get_user_id_by_email(email)
    item = crud.get_item_by_name(current_item)
    item_amount = request.form.get("add-to-cart")

    if "current_user" in session:
        crud.add_item_to_cart(item_id, user_id, item_amount)
        flash("Item added to cart!")
        return redirect("/shopping-cart")
    elif "current_user" not in session:
        flash("Please login.")
        return render_template('homepage.html', current_user = None)


@app.route("/category-info/<current_category>", methods = ["GET"])
def categoryInfo(current_category):
    """Displays items fitting a category."""

    category = crud.get_category_by_name(current_category)
    items = crud.get_item_by_category(current_category)
    category_items = crud.get_item_names_by_category_name(current_category)

    if "current_user" in session and category != None:
        return render_template('category-info.html', 
                                current_user = "current_user",
                                category_name = category.category_name,
                                category_items = category_items)
    else:
        flash("Please login.")
        return render_template('homepage.html', current_user = None)


@app.route("/delete-cart", methods = ["POST"])
def deleteCart():

    email = session["current_user"]
    user_id = crud.get_user_id_by_email(email)

    if "current_user" in session:
        crud.delete_all_cart_items(user_id)
        flash("Items deleted!")
        return redirect("/shopping-cart")
    else:
        flash("Please login.")
        return render_template('homepage.html', current_user = None)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
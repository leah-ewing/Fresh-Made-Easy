# Fresh Made Easy

Fresh Made easy allows customers to customize food boxes for pickup from locations close to their homes with food from local farms and vendors around the Nashville area. The Google Maps API allows users to view pickup locations are around them, and see where locally an item has been sourced from. User's can choose to shop by category or by vendor, and upon checkout can choose their preferred pickup location and date that works best for them.

## About Me

Leah has made her way to the tech industry in a bit of an untraditional way. She began working in kitchens in 2008  and since then has climbed the ladder in the culinary industry, cooking at a Five-Star hotel, and ultimately becoming the Executive Chef over a popular Nashville brewery's restaurant and event space. Over the course of working her way up in the hospitality scene, her role became more and more focused on problem solving--something that excited her. After an unforeseen global pandemic flipped the culinary scene on its head, and taking JavaScript up as a hobby during quarantine, she's looking to take her love of technology and problem solving to the next level and pursue a career in software engineering.


## Contents
* [Tech Stack](#tech-stack)
* [Features](#features)
* [Youtube Walkthough](#youtube-walkthrough)
* [Future Plans](#future-plans)
* [Installation](#installation)






## <a name="tech-stack"></a>Technologies

* Python
* JavaScript
* JQuery
* Jquery
* SQLAlchemy
* PostgresQL
* Bootstrap
* HTML
* CSS
* Bootstrap
* React
* Flask
* Google Maps API



## <a name="features"></a>Features

#### Homepage
Entering the homepage, users can view the "About Us" page for the site, the "How it Works" page, or take a sneak peak at the local pickup-locations and vendors. Users can create a new account via the "Sign Up" link or they can choose to login with an existing account.
# <img src="https://github.com/leah-ewing/Fresh-Made-Easy/blob/master/media/homepage.gif?raw=true" width="90%" alt="Homepage GIF"> 

#### View Pickup Locations
This page allows a user to view a list of all available pickup locations and see them on the Google Map. Clicking on a location brings up that location's information page and shows its exact location on the map.
# <img src="https://github.com/leah-ewing/Fresh-Made-Easy/blob/master/media/pickup-locations.gif?raw=true" width="90%" alt="Pickup Locations GIF"> 

#### View Local Vendors
This is where a user can view all local vendors that have items available for purchase and locations can be seen on the Google Map. Clicking on a vendor shows the vendor's information page and shows its exact location on the map. If a user is logged in, this page will also show a list of all items available from that vendor.
# <img src="https://github.com/leah-ewing/Fresh-Made-Easy/blob/master/media/view-vendors.gif?raw=true" width="90%" alt="Local Vendors GIF">

#### User Profile
A user's profile page allows them to view their shopping cart and previous purchases
# <img src="https://github.com/leah-ewing/Fresh-Made-Easy/blob/master/media/user-profile.gif?raw=true" width="90%" alt="User Profile GIF">

#### Shop Page
Users choose to shop by category, vendor, or browse through all items. Clicking on an item shows more information on it and give it's exact sourced location on the map.
# <img src="https://github.com/leah-ewing/Fresh-Made-Easy/blob/master/media/shop.gif?raw=true" width="90%" alt="Shop GIF">

#### Checkout Page
When users are ready to place their order, the checkout page allows them to choose their preferred pickup location and date. After a user checks out they can review their purchases in their profile.
# <img src="https://github.com/leah-ewing/Fresh-Made-Easy/blob/master/media/checkout.gif?raw=true" width="90%" alt="Checkout GIF">


## <a name="youtube-walkthrough"></a>Youtube Walkthrough
```
https://youtu.be/4UAE9usVyLg
```

## <a name="future-plans"></a>Future Plans

Here is a sneak peak of some future features planned for Fresh Made Easy:
* Implement admin login access to allow new pickup locations and vendors to update their own inventory and profile information
* Add a rating system to items, vendors, and pickup locations
* Option for a randomized boxes fitting a given price-point
* Delivery



## <a name="installation"></a>Installation

To run Fresh Made Easy on your local machine:

Install PostgresQL (Mac OSX)


Clone or fork this repo:
```
https://github.com/leah-ewing/Fresh-Made-Easy.git
```


Create and activate a virtual environment inside your JobTracker directory:
```
virtual env
source env/bin/activate
```


Install the dependencies:
```
pip install -r requirements.txt
```


Sign up to use the [Google Maps JavaScript API](https://developers.google.com/maps/documentation/javascript/overview), [Google Maps Embed API](https://developers.google.com/maps/documentation/embed/get-started)


Insert your API key into iframes in `farm-info.html`, `item-info.html`, `pickup-location-info.html`
```
<iframe
  width="600"
  height="450"
  style="border:0"
  loading="lazy"
  allowfullscreen
  src="https://www.google.com/maps/embed/v1/place?key=API_KEY
    &q=Sinema">
</iframe>
```


Insert your API key into scripts in `all-farms.html`, and `all-pickup-locations.html`
```
<script
  async defer
  src = "https://maps.googleapis.com/maps/api/js?key=API_KEY&callback=initFarmMap">
</script>
```


Set up the database:
```
createdb fresh
python3 seed_database.py
```


Run the app:
```
python3 server.py
```


You can now navigate to 'localhost:5000/' to access Fresh Made Easy!


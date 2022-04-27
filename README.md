# Home(ish)

## Introduction
The idea behind Home(ish) is to provide luxury furniture to renters and landlords, who enjoy lavish items and don't want to skimp out just because they are renting. To make this a stronger business case, the Home(ish) brand is also offering a upcycling, buy back scheme, where renters can sell items back to Home(ish) and a fraction of the cost they bought it for and Home(ish) manufacturers will repair the furniture to a high quality, to which it could be sold again to new customers. If the piece of furniture is not in a resellable state, the renter can still receive some money back for their items, but Home(ish) will recycle the furniture where possible. The aim is to reduce carbon footprint, while upholding a luxurious feel to the products Home(ish) sells. The brand is also in conjuction with Earthly.org, a carbon footprint charity. So, where we can donate items to their cause, or help raise money for them, we do.

[Home(ish) Website](https://homeish.herokuapp.com/)

Please see the Home(ish) initial business model below, created using Miro.

(Insert business model)

## User Stories & Project Goals
Before starting this project, it was important to understand what the purpose of the brand was, how could the user benefit, what else would the user need to feel satisfied from using the website and what considerations would developers need to take on to build a website that fulfilled all needs.

During planning there were some tasks that could not be fulfilled due to timing and they are listed in the Future Features section of this report.

User Story | Project Goals
---------- | ----------
As a user, I want to be able to login and see my past orders. | This was achieved by creating a profile for every user who registered an account with Home(ish) and they can see all the orders they have made on site since registering.
As a customer, I want to be able to search for a variety of items that can help kit out my new home. | This was achieved by uploading over 200 items of different pieces of furniture to the products.json file.
As a landlord, I want to be able to find items listed into categories, so that I can reduce my time searching for items I need. | This was achieved by creating categories in the main navigation bar, so that users can choose which specific pieces of furniture they were after, instead of browsing the full catalogue.
As a user, I want to be able to search for an item using a key word, to find items that are most revelant to my search. | This was achieved by including a search bar, which is a form, and when a user typed in keywords, items that have a name or description that matched those keywords, would appear in the search results.
As a user, I want to be able to see a live update of how many items are in my shopping cart and the subtotal to see how much I'm estimated to spend. | This was achieved by creating toasts, which display the number of items in the basket, the name and photo of the items added, as well as the subtotal, to show the user what's currently in their shopping cart and how much their cart totals to.
As a user, I want to be able to make secure payments on the website, in the fewest steps possible. | This was achieved by adding the delivery information and overview of the user's shopping cart on one page (checkout page) and using Stripe's payment software to handle payments, which is secure. The journey from shopping cart to successfull payment can take as less as 2 minutes.
As a user, I want to be able to get an idea of how I could style some of these items in my new home, so that I can buy with confidence. | This was achieved by creating an in-home service, where designers from Home(ish) can visit people in their homes and give advice on what furniture or décor pieces they should buy. This is done through the user making an appointment on the website, which they can then edit or delete and they are alerted of making any changes.

The initial draft of user stories is captured below.

(Insert user stories excel sheet)

## Project Design
The project design is split into 3 parts: the appearance of the website, access levels and the structure of the database.

### The Appearance
* The colour scheme used for this project derived from research that concluded purple is considered a luxury/royal colour. Hence why it was the main colour featured throughout the website. The idea behind it is, if the user can sense the luxury feeling of website, they will trust they will receive luxury goods.

* The Home(ish) brand font was chosen, due to the calligraphy that is common when you see elder people with a priviledged education background. Hoping that the font will captivate the user and entice them to browse the website. The main target audience is people with a considerable amount of disposable income, which is likely to be users in their late 30s and onwards. Given the price point of the furniture, it would make sure to target this audience.

* The product images are from MADE.com and they are reputable brand, known to sell expensive furniture, so it seemed appropriate to use their items, as their products and packshot photos are very professional and high-end.

* The opening image on the index page, with the white doors, is meant to emulate a clean, luxury feeling with the opportunity to design your space however you like. However, on smaller screens, a different image is used as the white door image is not as obvious when rendered for small screens.

* The initial design of the website is pictured below. As you browse through the homepage and the category pages, you will be able to see the structure is fairly similar but tweaked to match the improved Home(ish) brand design.

(Insert initial Home(ish) design)

### Role Access
* Majority of the website functionality is available to users who are not logged in. This is to maximise sales on the website with fewer barriers in place. However, if the user is not logged in nor created an account, they will not be able to see their past orders on the website.

* Additionally, the user will not be able to make an appointment with an in-home Home(ish) designer, as this requires a user to be logged in, so that they can manage and track their appointments.

* Furthermore, the admin of the website have their own access, which allows them to add, edit and delete products on the website. They also have the ability to state if an item is on sale or a new arrival, by selecting a drop down option. If they do this, items will appear with the appropriate tag under the product rating.

* Non-admin users cannot access pages that only an admin can use and this done by stating in the code, if the user is not a superuser, they will be told that this page is unaccessible to them and be redirected to the home page.

* Non logged in users cannot access content that is for logged in users, as the code specifies that the user needs to be logged in to view content `@login_required`. If they attempt to, they will have the option to go back to the home page via a link on the server error 500 page.

* If any user, including the admin, types in an incorrect url address, they will be served an 404 error page, with the opportunity to go back to the home page.

### Database Structure
In this project there are 3 main databases. The order database, the in-home design booking database and the products database.

#### The Order Database
* The order database gives visibility to the admin on all the orders that have been made on the website by logged in and non-logged in users. The Anonymous user was not logged in when making a purchase.

* When you click on the order number, you can see the detail of the user's delivery address, assign them to a user, if need be, the cost of the order and the specific items they bought. If a user has made an error in their purchase, it is possible to select a new product from the drop down list, as this model is linked to the products model. 

* If the product was to be deleted, it will no longer appear as an option to select in this model, due to the ForeignKey relationship.

#### The Appointments Database
* The appointment database view allows the admin to see which designer have appointments booked and with which user.

* If the admin were to delete a designer from the model list, then all appointments made with that designer will also be deleted. This is due to the ForeignKey relationship between the Appointments model and the Designer model.

#### The Products and Categories Database
* Given the vast data appened to each product, it's important to know what category each product falls under, is it also on sale or a new arrival, what's the current price and rating etc. Similar to the appointments model, if a category is no longer available and is deleted, the products under this category will also be deleted. Once again due to the ForeignKey relationship.

## Current Features
<details>
<summary>Features</summary>

### Homepage
* The homepage is the first page the user will see when landing on the site. So, it has to be clear what the purpose is so they know whether they want to stay on the website or not.

* There is also a small blurb on the homepage to explain more about the purpose of the site, to mitigate any concerns on what the website is about.

* There is an opportunity for the user to sign up to Home(ish)'s newsletter and subscribe. This functionality was built using MailChimp. In a real world project, the user would be sent regular updates about new stock available, sales, the partnership with Earthly.org etc.

* Following on from this, the user is exposed some décor images and a glimpse of some of the content on Home(ish)'s social media pages. Additionally, there are 3 icons of the social pages Home(ish) has, which the user can explore.

### All Products
* The all products page essentially lists all the products in the store's catalogue. There is an opportunity for the user to sort the list in 4 ways, by price (low or high), by rating (low or high), by name (A-Z) and by category (A-Z). So, if a user is looking to see the least expensive products on site, they can it with ease and can continue exploring what products Home(ish) has by playing with the sorting.

* Each product has a picture, name, price, category, rating and if it's on sale or a new arrival. The item is on sale, the original price will be striken through and in light grey. This is to make it obvious to the user what the current price is.

* In the admin's view, they will also see an option to edit or delete the product, which won't be visible to a non superuser. This is to prevent non superuser's from editing the catalogue in any way.

* Depending on the screen size the user is visiting the website on, they will either see an array of 4 products per line (desktop and larger screens), down to 1 product, if viewing on mobile.

### Categories
* There are 8 categories in total. Each category has a minimum of 15 items, so there is a variety a user can choose from.

* Each category has it's own page and header, so the user knows what items to expect on the page.

* Once again, the user can use the sorting functionality to reorganise the position of the products on the page.

### Décor Inspiration
* This page was created to give users inspiration on how they could decorate their home. The more pictures that inspire them, the more likely they will want to add more products to their shopping cart to replicate the décor images.

* This page also presents the opportunity for users to book an in-home design with one of Home(ish) designers. If the user is logged in they will be directed to the appointment booking page. If the user is not logged in, then they will be directed to login/create an account first, before they can proceed to make an appointment. This is because the user needs an account to see the bookings they have made with the store.

### Contact Us
* The contact us page, allows users to send messages to Home(ish) regarding any questions they have, including the buy back scheme. Currently there isn't a feature for users to submit a form on the list of products they wish to sell back and the estimated price they could get for it.

### Appointments
* The appointments page, is a short form the user will need to fill out. Once successfully submitted, the user will be directed to a page where they can see all the bookings they have made. They will also have the opportunity to edit and/or delete bookings. If they have no upcoming bookings, they will have the option to make an appointment from this page.

### Profile
* In the profile page non superuser's will see their past orders and their delivery information. They can update their delivery information as often as they need to.

* The superuser, also know as the admin, will have an additional page accessible to them, where they can choose to add products to the website, simply by filling out a form. They can also choose the edit products. If they do they will shown a similar view, with the fields prefilled and they can choose what needs editing. Once they have made their changes, they can click update and the changes will be reflected in the main products view. Updates are made instantaneously.

### Shopping Cart
* The shopping cart displays the item(s) added to the cart, the sku number, price, quantity and subtotal. Additionally, it shows the bag total, any delivery costs, discounts awarded and the grand total.

* The current promotion on the website is that if the user's subtotal is greater than £350, then the user is awarded free delivery and £50 off their grand total. If the user does not have a cart value of at least £350, then they will need to pay a delivery fee that is 20% of the current subtotal value.

* Additionally, if the user is close to the £350 mark to be awarded the discount, there will be a message telling the user, the remaining amount they will need to spend. This is also flagged to the user in the toast, when they add something new to their shopping cart.

### Checkout
* The checkout page has a small form for the user to fill out. Their name, email and delivery information. It also shows an overview of the items the user has added to their shopping cart, any discounts awarded and if they have a delivery charge.

* The user can also add in their payment information to finish the checkout stage. The website won't be able to start processing payments until every necessary/required field has valid input from the user.

* Once the order has gone through successfully, the user will be redirected to the checkout success page and see a confirmation page of the items they ordered, along with the delivery address and how much they will be charged. It also notifies the user that a confirmation email will be sent to the email address they inputted at checkout stage.

* There is also an opportunity to drive users back to the product page with the CTA button on the button of the confirmation page. This is to entice users to check the product page again and purchase anything they may have been hesitating on before, or forgot to purchase.

### Footer
* The footer is available on every page as it is part of the base.html doc. It has information of Home(ish)'s privacy policy, contact page, the link to Earthly.org charity page, their 3 social pages and the Home(ish) in-home design service. This information was chosen to be in the footer, so the user always has access to these links no matter what page they are on.

### Main Navigation Bar
* The main navigation bar displays the brand name, the option to click on the product catalogue, the categories, the décor inspiration, contact page, appointment page, profile page and the shopping cart. Once again, these links are available on every page as it's part of the base.html doc. The user will have access to all necessary links either via the main navigation bar or the footer.

### Login/Logout/Sign Up
* The signing up process is very straightforward. If the user is not currently logged in, there will be an option to either sign up/register or login. Once the user has created an account and is logged in, they will have the option to logout. This is reflected on the profile icon.

* The user is also notified via toasts messages when they have logged in, so it's clear to the user that the logging in process was successful. The same happens when the user logs out, they see a toast telling them they have successfully signed out.

</details>

## Future Implementations
* To include a wishlist page, so users can favourite items that they would like to purchase in the future.

* To include a comment section on the product detail page, so users can leave reviews on the specific products and other users could choose to like the comments.

* To include a frequently asked questions page, as users may have common questions. This will help reduce traffic to the contact us page, as most questions would have been already answered and on display for the user.

* To include a stock count of each product and every time that product was purchased the stock count would reduce by 1. Then when the stock count was 5 or less, a note or tag on the image would say low stock. This could help entice users to buy that product as not to risk missing out.

## Testing
<details>
<summary>Manual Tests Conducted</summary>

</details>

<details>
<summary>Automated Tests Conducted</summary>

</details>

### Validation Checks
* HTML W3C Validator – No errors found

* CSS3 Jigsaw Validator – No errors found

* Pep8 – No errors found, except for the placeholder attribute in the design form for 'designer' and 'time'. 

* JShint – No errors found

* Heroku works correctly as planned across Google Chrome, Safari, Microsoft Edge and Mozilla Firefox

* Tested the Heroku program on iPhone 12, Google Pixel 2, Motorola Edge and Huawei P9

## Project Bugs & Solutions

### Resolved
Bugs | Solutions
-------- | --------
The product model originally only had price. So when I applied the sale discount to some products, the price would reduce as planned by 15% but if the user wanted to sort the products by price, the order wouldn't be correct, as the computer was taking into account the old price and not the new price. | To overcome this, I needed to create an additional field in the product model called 'current price'. This allowed me to set non sale items to the current price and change sale items to 'price'. I then arranged the price sorting feature on 'current price' instead of just 'price' and the price ordering works perfectly.
The décor images on the décor inspiration page on homepage were originally not showing, even after uploading the assets to amazon web services (AWS). | I realised I needed to add `{{ MEDIA_URL }}` in front of the image name, so that it will appear on the heroku website.

### Unresolved
Bugs | Ideal Solution
-------- | --------
On the product detail page, users are limited to add 50 of each product to their shopping cart. This works perfectly fine. However, the user can override this and add more than 50 on the shopping cart page. After implementing the revised code suggested by Code Institute, the user can extend past the JavaScript limit and add a quantity greater than 50 by manually typing in the value. | Ideally the limit would be enforced on the shopping cart page, but for now, this is currently not in place.

## Deployment
<details>
<summary>Step-by-step</summary>

Section | Number | Step | Code | Notes
-------- | -------- | -------- | -------- | --------

</details>

## Technologies Used
* HTML5

* CSS3

* JavaScript

* Python3

* Django

* Postgres

## Credits

### Code
* Code Institute tutorial videos
* CSS code for the footer from Colorlib.com

### Images
* Unsplash.com
* Made.com

### Content
* Self created content, except for product descriptions, which came from Made.com.

### Acknowledgements
* My mentor Rahul for his ongoing support and feedback

* The Code Institute’s Tutor Support

* The Slack community
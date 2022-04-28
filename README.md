# Home(ish)

## Introduction
The idea behind Home(ish) is to provide luxury furniture to renters and landlords, who enjoy lavish items and don't want to skimp out just because they are renting. To make this a stronger business case, the Home(ish) brand is also offering a upcycling, buy back scheme, where renters and landlords can sell items back to Home(ish) at a fraction of the cost they bought it for. Home(ish) manufacturers will then repair the furniture to a high quality, to which it could be sold again to new customers. If the piece of furniture is not in a resellable state, the renter/landlord can still receive some money back for their items, but Home(ish) will recycle the furniture where possible. The aim is to reduce carbon footprint, while upholding a luxurious feel to the products Home(ish) sells. The brand is also in conjuction with Earthly.org, a carbon footprint charity. So, where we can donate items to their cause, or help raise money for them, we do.

![image](https://user-images.githubusercontent.com/81588887/165587950-a38e8c93-c892-4e5c-8c89-5878514dc7a7.png)

[Home(ish) Website](https://homeish.herokuapp.com/)

Please see the Home(ish) initial business model below, created using Miro.

![image](https://user-images.githubusercontent.com/81588887/165588031-226dc6d2-6228-4f5c-b257-26d0b630c52b.png)

## User Stories & Project Goals
Before starting this project, it was important to understand what the purpose of the brand was, how could the user benefit, what else would the user need to feel satisfied from using the website, and what considerations would developers need to take on to build a website that fulfilled all needs.

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

<img width="980" alt="image" src="https://user-images.githubusercontent.com/81588887/165588245-2d7de5a6-588b-4ac2-8feb-a33b51fcbb7e.png">

## Project Design
The project design is split into 3 parts: the appearance of the website, access levels and the structure of the database.

### The Appearance
* The colour scheme used for this project derived from research that concluded purple and gold are considered luxury/royal colours. Hence why the colours were featured throughout the website. The idea behind it is, if the user can sense the luxury feeling of website, they will trust they will receive luxury goods.

![image](https://user-images.githubusercontent.com/81588887/165588440-7ce45388-70bd-4008-8171-6a1450f1040e.png)

* The Home(ish) brand font was chosen, due to the calligraphy that is common when you see elder people with a priviledged education background. Hoping that the font will captivate the user and entice them to browse the website. The main target audience is people with a considerable amount of disposable income, which is likely to be users in their late 30s and onwards. Given the price point of the furniture, it would make sure to target this audience.

![image](https://user-images.githubusercontent.com/81588887/165588522-ebe4c567-dd9e-4404-8d60-d5cdfcbfff91.png)

* The product images are from MADE.com and they are reputable brand, known to sell expensive furniture, so it seemed appropriate to use their items, as their products and packshot photos are very professional and high-end.

* The opening image on the index page, with the white doors, is meant to emulate a clean, luxury feeling with the opportunity to design your space however you like. However, on smaller screens, a different image is used as the white door image is not as obvious when rendered for small screens.

![image](https://user-images.githubusercontent.com/81588887/165588714-d4e33591-ce64-4b79-8836-a30c8237a5dc.png)

* The initial design of the website is pictured below. As you browse through the homepage and the category pages, you will be able to see the structure is fairly similar but tweaked to match the improved Home(ish) brand design.

<img width="993" alt="image" src="https://user-images.githubusercontent.com/81588887/165589937-e68ac483-6b66-4ff3-877f-30dbd7bff115.png">
<img width="989" alt="image" src="https://user-images.githubusercontent.com/81588887/165590019-6172607a-df5e-477f-8d51-5f4972d58099.png">
<img width="973" alt="image" src="https://user-images.githubusercontent.com/81588887/165590095-a532fe8c-aeaf-4125-a91d-e29933ea80fd.png">

### Role Access
* Majority of the website functionality is available to users who are not logged in. This is to maximise sales on the website with fewer barriers in place. However, if the user is not logged in nor created an account, they will not be able to see their past orders on the website.

* Additionally, the user will not be able to make an appointment with an in-home Home(ish) designer, as this requires a user to be logged in, so that they can manage and track their appointments.

* Furthermore, the admin of the website have their own access, which allows them to add, edit and delete products on the website. They also have the ability to state if an item is on sale or a new arrival, by selecting a drop down option. If they do this, items will appear with the appropriate tag under the product rating.

* Non-admin users cannot access pages that only an admin can use and this done by stating in the code, if the user is not a superuser, they will be told that this page is unaccessible to them and be redirected to the home page.

* Non logged in users cannot access content that is for logged in users, as the code specifies that the user needs to be logged in to view content `@login_required`. If they attempt to, they will have the option to go back to the home page via a link on the server error 500 page.

![image](https://user-images.githubusercontent.com/81588887/165591643-97843d9c-9ec7-4fed-bd8c-5a5ba5a549b1.png)

* If any user, including the admin, types in an incorrect url address, they will be served an 404 error page, with the opportunity to go back to the home page.

![image](https://user-images.githubusercontent.com/81588887/165590706-bff62974-4392-477b-a84c-cfbe67f1ff9e.png)

### Database Structure
In this project there are 3 main databases. The order database, the in-home design booking database and the products database.

#### The Order Database
* The order database gives visibility to the admin on all the orders that have been made on the website by logged in and non-logged in users. The Anonymous user was not logged in when making a purchase.

![image](https://user-images.githubusercontent.com/81588887/165591868-e5a38d51-5c50-4a8d-9636-1a8c3f12a672.png)

* When you click on the order number, you can see the detail of the user's delivery address, assign them to a user, if need be (this can be done to the one2one relationship between the order model and the user profile model), the cost of the order and the specific items they bought (connection made via the order line item model - foreign key). If a user has made an error in their purchase, it is possible to select a new product from the drop down list, as this model is linked to the products model. 

* If the product was to be deleted, it will no longer appear as an option to select in this model, due to the ForeignKey relationship between product and order line item.

![image](https://user-images.githubusercontent.com/81588887/165592018-ee8e0ba6-75f6-496a-8dab-7818f66cb304.png)

#### The Appointments Database
* The appointment database view allows the admin to see which designers have appointments booked and with which user.

* If the admin were to delete a designer from the model list, then all appointments made with that designer will also be deleted. This is due to the ForeignKey relationship between the Appointments model and the Designer model.

![image](https://user-images.githubusercontent.com/81588887/165592122-71003fed-ac5b-484c-a9d5-9fae56ce3b93.png)

#### The Products and Categories Database
* Given the vast data appened to each product, it's important to know what category each product falls under, is it also on sale or a new arrival, what's the current price and rating etc. Similar to the appointments model, if a category is no longer available and is deleted, the products under this category will also be deleted. Once again due to the ForeignKey relationship.

![image](https://user-images.githubusercontent.com/81588887/165592192-408aa7cd-e968-40d7-acaa-a85baf35d6de.png)
![image](https://user-images.githubusercontent.com/81588887/165592254-be079c86-42ba-4c0f-ab75-cb6c8c9a3875.png)

Full Database Schema (made using LucidChart)
<img width="789" alt="image" src="https://user-images.githubusercontent.com/81588887/165623522-85ea2ddf-4dc7-4aae-ba50-e6de0374f1ca.png">

## Current Features
<details>
<summary>Features</summary>

### Homepage
* The homepage is the first page the user will see when landing on the site. So, it has to be clear what the purpose is so they know whether they want to stay on the website or not.

* There is also a small blurb on the homepage to explain more about the purpose of the site, to mitigate any concerns on what the website is about.

![image](https://user-images.githubusercontent.com/81588887/165592344-20facb56-8e91-42ae-bbe8-af4c3f6657f3.png)

* There is an opportunity for the user to sign up to Home(ish)'s newsletter and subscribe. This functionality was built using MailChimp. In a real world project, the user would be sent regular updates about new stock available, sales, the partnership with Earthly.org etc.
  
![image](https://user-images.githubusercontent.com/81588887/165592466-0ee12384-0d02-4be4-957b-ed6ac80b3996.png)

* Following on from this, the user is exposed some décor images and a glimpse of some of the content on Home(ish)'s social media pages. Additionally, there are 3 icons of the social pages Home(ish) has, which the user can explore.
  
![image](https://user-images.githubusercontent.com/81588887/165592522-2fa58c2a-324d-4698-8c61-aad4ce80ec79.png)

### All Products
* The all products page essentially lists all the products in the store's catalogue. There is an opportunity for the user to sort the list in 4 ways, by price (low or high), by rating (low or high), by name (A-Z) and by category (A-Z). So, if a user is looking to see the least expensive products on site, they can it with ease and can continue exploring what products Home(ish) has by playing with the sorting.
  
![image](https://user-images.githubusercontent.com/81588887/165592818-dd992647-29b9-431e-9cb5-35ce182801e2.png)

* Each product has a picture, name, price, category, rating and if it's on sale or a new arrival. The item is on sale, the original price will be striken through and in light grey. This is to make it obvious to the user what the current price is.

* In the admin's view, they will also see an option to edit or delete the product, which won't be visible to a non superuser. This is to prevent non superuser's from editing the catalogue in any way.

* Depending on the screen size the user is visiting the website on, they will either see an array of 4 products per line (desktop and larger screens), down to 1 product, if viewing on mobile.
  
![image](https://user-images.githubusercontent.com/81588887/165592751-6328eacd-2436-4802-abbd-16bfb187bec8.png)

### Categories
* There are 10 categories in total. However, 2 of these categories are for labelling purposes, 'Sale' and 'New Arrivals'. Each category has a minimum of 15 items, so there is a variety a user can choose from.
  
![image](https://user-images.githubusercontent.com/81588887/165593011-da23b077-1cb9-43b1-a040-55c737686f7d.png)

* Each category has it's own page and header, so the user knows what items to expect on the page.

* Once again, the user can use the sorting functionality to reorganise the position of the products on the page.
  
![image](https://user-images.githubusercontent.com/81588887/165593153-88584e80-7a41-4b1c-961a-796b3c97d8de.png)

### Décor Inspiration
* This page was created to give users inspiration on how they could decorate their home. The more pictures that inspire them, the more likely they will want to add more products to their shopping cart to replicate the décor images.

* This page also presents the opportunity for users to book an in-home design with one of Home(ish) designers. If the user is logged in they will be directed to the appointment booking page. If the user is not logged in, then they will be directed to login/create an account first, before they can proceed to make an appointment. This is because the user needs an account to see the bookings they have made with the store.
  
![image](https://user-images.githubusercontent.com/81588887/165593326-92042ce2-aa4b-4575-9777-d9d439e1e9bb.png)
(logged in)

![image](https://user-images.githubusercontent.com/81588887/165593431-431398e3-4d38-4441-9dfa-af0a219c5156.png)
(logged out or have not registered an account yet)

### Contact Us
* The contact us page, allows users to send messages to Home(ish) regarding any questions they have, including the buy back scheme. Currently there isn't a feature for users to submit a form on the list of products they wish to sell back and the estimated price they could get for it.
  
![image](https://user-images.githubusercontent.com/81588887/165593565-82ba03bd-9167-4256-93e4-afdc8f936099.png)

### Appointments
* The appointments page, is a short form the user will need to fill out. Once successfully submitted, the user will be directed to a page where they can see all the bookings they have made. They will also have the opportunity to edit and/or delete bookings. If they have no upcoming bookings, they will have the option to make an appointment from this page.
  
![image](https://user-images.githubusercontent.com/81588887/165593705-4226651d-e3dd-479e-9061-4275d19bd928.png)
![image](https://user-images.githubusercontent.com/81588887/165593831-0011cd0b-b6cc-4e66-b16d-909282f32137.png)
![image](https://user-images.githubusercontent.com/81588887/165593907-e4f72bb0-2273-4569-979c-6953946ddb19.png)

### Profile
* In the profile page, logged in users will see their past orders and their delivery information. They can update their delivery information as often as they need to.
  
![image](https://user-images.githubusercontent.com/81588887/165594192-e01534d5-f007-4090-8f7e-23d920e31039.png)

* The superuser, also know as the admin, will have an additional page accessible to them, where they can choose to add products to the website, simply by filling out a form. They can also choose the edit products. If they do they will shown a similar view, with the fields prefilled and they can choose what needs editing. Once they have made their changes, they can click update and the changes will be reflected in the main products view. Updates are made instantaneously.
  
![image](https://user-images.githubusercontent.com/81588887/165594330-bb331021-1e41-493a-8ff7-5ce08f47fe79.png)

### Shopping Cart
* The shopping cart displays the item(s) added to the cart, the sku number, price, quantity and subtotal. Additionally, it shows the bag total, any delivery costs, discounts awarded and the grand total.

* The current promotion on the website is that if the user's subtotal is greater than £350, then the user is awarded free delivery and £50 off their grand total. If the user does not have a cart value of at least £350, then they will need to pay a delivery fee that is 20% of the current subtotal value.

* Additionally, if the user is close to the £350 mark to be awarded the discount, there will be a message telling the user, the remaining amount they will need to spend. This is also flagged to the user in the toast, when they add something new to their shopping cart.
  
![image](https://user-images.githubusercontent.com/81588887/165594571-c24a4d28-66a5-407e-b144-e3f266864a4e.png)
(shopping cart subtotal is greater than £350, so the user gets free delivery and a £50 discount)
![image](https://user-images.githubusercontent.com/81588887/165594877-d349ea89-b531-4b92-a9a4-260bb7edfc57.png)
(shopping cart subtotal is less than £50, so the user is charged an addiional 20% delivery fee and receives no discount)

### Checkout
* The checkout page has a small form for the user to fill out. Their name, email and delivery information. It also shows an overview of the items the user has added to their shopping cart, any discounts awarded and if they have a delivery charge.

* The user can also add in their payment information to finish the checkout stage. The website won't be able to start processing payments until every necessary/required field has valid input from the user.
  
![image](https://user-images.githubusercontent.com/81588887/165595336-5b9493da-91c8-4183-be3f-add6cf5a2ab3.png)

* Once the order has gone through successfully, the user will be redirected to the checkout success page and see a confirmation page of the items they ordered, along with the delivery address and how much they will be charged. It also notifies the user that a confirmation email will be sent to the email address they inputted at checkout stage.

* There is also an opportunity to drive users back to the product page with the CTA button on the button of the confirmation page. This is to entice users to check the product page again and purchase anything they may have been hesitating on before, or forgot to purchase.
  
![image](https://user-images.githubusercontent.com/81588887/165595653-88fd4cf0-f1de-452c-b9f1-ab449aaddfdd.png)
![image](https://user-images.githubusercontent.com/81588887/165595722-cd2d969e-28de-45dc-b76c-c4e71e8e6aa7.png)

### Footer
* The footer is available on every page as it is part of the base.html doc. It has information of Home(ish)'s privacy policy, contact page, the link to Earthly.org charity page, their 3 social pages and the Home(ish) in-home design service. This information was chosen to be in the footer, so the user always has access to these links no matter what page they are on.
  
![image](https://user-images.githubusercontent.com/81588887/165595793-1c7ab6ce-1e60-48e4-bcff-5f32ff3941d7.png)
(desktop or tablet view)
![image](https://user-images.githubusercontent.com/81588887/165596136-92505df8-43cd-4f0e-8c3b-2c39447fdaeb.png)
(mobile view)

### Main Navigation Bar
* The main navigation bar displays the brand name, the option to click on the product catalogue, the categories, the décor inspiration, contact page, appointment page, profile page and the shopping cart. Once again, these links are available on every page as it's part of the base.html doc. The user will have access to all necessary links either via the main navigation bar or the footer.
  
![image](https://user-images.githubusercontent.com/81588887/165595877-d3f467ee-83c3-4373-b5f6-980fb0ab8f7d.png)
(desktop or tablet view)
![image](https://user-images.githubusercontent.com/81588887/165595970-49dbd2ab-d233-4764-aac5-9b1a2011b168.png)
(mobile view)

### Login/Logout/Sign Up
* The signing up process is very straightforward. If the user is not currently logged in, there will be an option to either sign up/register or login. Once the user has created an account and is logged in, they will have the option to logout. This is reflected on the profile icon.
  
![image](https://user-images.githubusercontent.com/81588887/165596293-b9d7e425-c659-4cef-837c-ce6353bebc76.png)
(login view)
![image](https://user-images.githubusercontent.com/81588887/165596407-8f7eed79-a2ce-4386-957f-6c88cb380afb.png)
(sign up view)
![image](https://user-images.githubusercontent.com/81588887/165596533-974567ab-a6e5-46a1-9895-b8213aaa8412.png)
(logout view)

* The user is also notified via toasts messages when they have logged in, so it's clear to the user that the logging in process was successful. The same happens when the user logs out, they see a toast telling them they have successfully signed out.

</details>

## Social Media Pages

### Facebook
![image](https://user-images.githubusercontent.com/81588887/165603272-db42a641-a4a1-49bb-9928-0b5401905289.png)
[Home(ish) Facebook Page](https://www.facebook.com/Home_ish-106704365332388)

### Instagram
![image](https://user-images.githubusercontent.com/81588887/165603515-7a45898e-31e9-49e5-87c1-e9f865de6c0c.png)
[Home(ish) Instagram Page](https://www.instagram.com/home.ish_uk/)

### Pinterest
![image](https://user-images.githubusercontent.com/81588887/165603705-be3c0cbc-f859-4128-8703-5373df18d014.png)
[Home(ish) Pinterest Page](https://www.pinterest.co.uk/homeish_uk/_created/)

## Marketing Strategy
Given the brand's new launch, it's best to focus on cost-effective media channels that have scalable reach amongst Home(ish)'s target audiences. Social media can be cost-effective channel, if the brand focuses on building their organic social presence, but can also tap into paid social media to attract more users to their brand. With a budget of appoximately £50k to spend on social media and SEO marketing. It would be my recommendation to spend £20k on one social media to start with, preferably Facebook, given their is a plethora of our target audience on this platform already. We can do a brand awareness campaign across newsfeed and stories posts to start with, while doing split testing against our two audiences, renters and landlords and see which audience has become more aware of the brand. Once we have this established, we can then funnel more budget into the winning audience and prioritise them in future paid social marketing practices. If we see Facebook perform well, then we can see if the same two audiences are active on Instagram and Pinterest and adjust budget to them accordingly.

For SEO, it can be more expensive, hence why I recommend putting £30k to start with behind it. This will give us access to not just SEO but also paid search and allow us to utilise Google's paid offerings that can help us determine what keywords we should use and bid against. Once we have an understanding on what terms is best for Home(ish)'s ranking in Google, we can then determine how much more budget to put into it effefctvely.

There is also the opportunity to do cross-channel attribution and see what marketing channels are driving the best results for Home(ish). This will determine how much budget each channel gets for the following year for marketing and advertising.

## Future Implementations
* To include a wishlist page, so users can favourite items that they would like to purchase in the future.

* To include a comment section on the product detail page, so users can leave reviews on the specific products and other users could choose to like the comments.

* To include a frequently asked questions page, as users may have common questions. This will help reduce traffic to the contact us page, as most questions would have been already answered and on display for the user.

* To include a stock count of each product and every time that product was purchased the stock count would reduce by 1. Then when the stock count was 5 or less, a note or tag on the image would say low stock. This could help entice users to buy that product as not to risk missing out.

## Testing
<details>
<summary>Manual Tests Conducted</summary>

Lanuague | Test | Outcome
-------- | -------- | --------
Other (MailChimp) | To successfully add user's email addresses to the Home(ish) MailChimp account | ![image](https://user-images.githubusercontent.com/81588887/165596640-602dc54d-4674-4b6f-b716-b37817f0a899.png)
JavaScript | To successfully sort products based on the filter, inparticularly by price | ![image](https://user-images.githubusercontent.com/81588887/165596781-50f6b226-cb16-4341-a561-e5ccd8d679b4.png)
JavaScript | To restrict users to 50 items of the same product in one shop | ![image](https://user-images.githubusercontent.com/81588887/165596896-fe2f0c91-270d-4d2b-972a-f509f3d9346f.png)
Email JS | To successfully receive emails from users and notify the user their email was sent successfully | ![image](https://user-images.githubusercontent.com/81588887/165597662-23b89e0e-d8d1-4069-b8a3-75cbe0c7c749.png)![image](https://user-images.githubusercontent.com/81588887/165597763-d24cdce6-f5eb-49b5-aa0c-eee375198ab4.png)
Django | To create, edit and delete an appointment form | ![image](https://user-images.githubusercontent.com/81588887/165597945-49e34e16-ddda-4bc3-aa9a-533bf192af80.png)![image](https://user-images.githubusercontent.com/81588887/165598014-f8952dbb-976f-4335-bc5a-052cf37ea767.png)![image](https://user-images.githubusercontent.com/81588887/165598116-9d3778c0-d30f-42f9-a2d2-5a6b7c06c8d3.png)![image](https://user-images.githubusercontent.com/81588887/165598162-70e86544-1cf4-48bb-9584-e92518fb18df.png)
Django | The admin can add, edit and delete products with ease | ![image](https://user-images.githubusercontent.com/81588887/165598346-06bf34c4-1e63-469b-97ef-d44e98452661.png)![image](https://user-images.githubusercontent.com/81588887/165598651-da7df2ac-174b-4ec2-9cd5-2f7886e628c7.png)![image](https://user-images.githubusercontent.com/81588887/165598442-331c7ea7-5311-44a2-aa95-c615e8bd0739.png)![image](https://user-images.githubusercontent.com/81588887/165598802-0609ed9e-ae5b-4176-9b4a-de4fdc75c7d5.png)
Django | The user can update their delivery information from their account page and this will be reflected when they next purchase from the website | ![image](https://user-images.githubusercontent.com/81588887/165599122-7a777f93-b2bd-4dff-9e4e-f915b1f34762.png)(added Thia Tower to the second street address line)![image](https://user-images.githubusercontent.com/81588887/165599249-294eb336-21a2-4196-82fd-5828735b4a3e.png)(Thia Tower now appears at the checkout stage automatically)
Django | To award users free delivery and a £50 discount when their subtotal is £350 | ![image](https://user-images.githubusercontent.com/81588887/165599428-a6144998-bc64-4580-b874-64e27d8bc8db.png)(subtotal is less than £350)![image](https://user-images.githubusercontent.com/81588887/165599518-d0c56c92-5629-4657-9ff4-f9e779dc6da9.png)(subtotal is greater than £350 and the user has free delivery and £50 off)
Other (Stripe) | To demonstrate that the website will accept or reject payments if the card details are valid or not | ![image](https://user-images.githubusercontent.com/81588887/165599828-e72ef13a-fc87-4f53-9979-95956b79baa7.png)(successfull test card payment details)![image](https://user-images.githubusercontent.com/81588887/165600097-1afaa7f4-ed6f-4acf-9e3c-efead128ef65.png)(declined test card payment details)
Other (Stripe) | Users will be sent confirmation emails with their order details if their payement was successfull | ![Screenshot 2022-04-27 at 20 02 22](https://user-images.githubusercontent.com/81588887/165600791-8e5f0049-cf9a-481e-beed-76b845082558.png)

</details>

<details>
<summary>Automated Tests Conducted</summary>

Automated test coverage was conducted at app level. The coverage report at the time of the project did not display the htmlcov folder, so individual screen shots have been attached instead.

### Checkout
![image](https://user-images.githubusercontent.com/81588887/165604794-32281c30-96d1-46d6-9c2a-d36a52127abe.png)

### Design
![image](https://user-images.githubusercontent.com/81588887/165604965-44e73172-e9f7-4e7b-bb3b-ba970a0048cb.png)

### Products
![image](https://user-images.githubusercontent.com/81588887/165605181-721af510-1de7-4628-976d-ff4710b47d46.png)

### Profiles
![image](https://user-images.githubusercontent.com/81588887/165605322-05856304-6555-4439-8a8f-35bad0354cc4.png)

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
Creating a Heroku App | 1 | Go to the heroku website and click new and then create new app |
Creating a Heroku App | 2 | Give your app a name and then chose a region closest to you |
Creating a Heroku App | 3 | On the resource tab, search for heroku postgres in the add ons bar and select the free plan |
Creating a Heroku App | 4 | Go back to Gitpod and type the following in the terminal | `pip3 install dj_database_url` then `pip3 install psycopg2-binary` and now freeze `pip3 freeze > requirements.txt` |
Creating a Heroku App | 5 | Go to settings.py and import dj_database_url | `import dj_database_url` |
Creating a Heroku App | 6 | Then scroll down to the Database section and comment out the default configuration and replace it with a call to dj_database_url.parse | `dj_database_url.parse()` | DATABASES = {'default': dj_database_url.parse('insert postgres url from heroku config vars under settings tab')} |
Creating a Heroku App | 7 | Now let's look at the outstanding migrations | `python3 manage.py showmigrations` |
Creating a Heroku App | 8 | Now migrate changes | `python3 manage.py migrate` |
Creating a Heroku App | 9 | Upload database, categories first and then products | `python3 manage.py loaddata categories` and then `python3 manage.py loaddata products` |
Creating a Heroku App | 10 | Now create a superuser to login with | `python3 manage.py createsuperuser` | Create a username and password to login in with later |
Creating a Heroku App | 11 | Now remove the new database code created and uncomment the original database code before committing to Github | | Delete this code from your settings.py - DATABASES = {'default': dj_database_url.parse('insert postgres url from heroku config vars under settings tab')} |
Creating a Heroku App | 12 | Commit to Github |
Deploying to Heroku | 1 | Use an if statement to determine which database the system will follow | | ![database code](https://user-images.githubusercontent.com/81588887/165558846-a5a124e2-0fc1-444c-8064-0aee23fdda4b.png)
Deploying to Heroku | 2 | Next install gunicorn | `pip3 install gunicorn` |
Deploying to Heroku | 3 | Freeze this install | `pip3 freeze > requirements.txt` |
Deploying to Heroku | 4 | Now create a Procfile in the root directory | | Procfile
Deploying to Heroku | 5 | Type the following into the new Procfile created | `web: gunicorn app_name.wsgi:application`
Deploying to Heroku | 6 | Now log into heroku via the terminal | `heroku login -i` |
Deploying to Heroku | 7 | Temporarily disable collect static | `heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku_app_name` |
Deploying to Heroku | 8 | Go to settings.py, scroll to 'ALLOWED HOSTS' and type in your heroku app url and local host | | ![image](https://user-images.githubusercontent.com/81588887/165560864-cb4d5ad8-a75a-44ce-a2f0-a561721db223.png)
Deploying to Heroku | 9 | Commit and push your changes through |
Deploying to Heroku | 10 | Then push to heroku's site | git push heroku main |
Deploying to Heroku | 11 | Setup automatically deploys by going to heroku's website and selecting the deploy tab |
Deploying to Heroku | 12 | Then set it to connect to Github and search for your repository and click connect |
Deploying to Heroku | 13 | Now you can set it to enable automatic deploys | | Now every time you push to Github, your Heroku app will also update and deploy |
Deploying to Heroku | 14 | Search on Google for a secret key generator, generate a key and then add it to a config variable in Heroku |
Deploying to Heroku | 15 | In Heroku, under settings, scroll to config vars and type in 'SECRET_KEY' for the key and copy in the secret key code in the value field, then click add |
Deploying to Heroku | 16 | Go back to settings.py and replace the value for the secret key to the following | `SECRET_KEY = os.environ.get('SECRET_KEY', '')`
Deploying to Heroku | 17 | Set debug to development if it's true in config vars | `DEBUG = 'DEVELOPMENT' in os.environ` |
Deploying to Heroku | 18 | Commit and push these changes through |
Creating an AWS Account | 1 | Go to aws.amazon.com and click on create an account. Proceed to fill in your details |
Creating an AWS Account | 2 | Sign into your account and in the search bar, type the following | S3 |
Creating an AWS Account | 3 | Select S3 and create a new bucket |
Creating an AWS Account | 4 | Give your bucket a name and select the region closest to you |
Creating an AWS Account | 5 | Then untick 'Block all public access' and tick that you acknowledge your bucket will be public |
Creating an AWS Account | 6 | Then click create bucket |
Creating an AWS Account | 7 | On the properties tab, select that you will use this bucket to host a website |
Creating an AWS Account | 8 | In the index.document field type | `index.html` |
Creating an AWS Account | 9 | In the error.document field type | `error.html` | | Now click save
Creating an AWS Account | 10 | On the permissions tab, select the CORS configuration tab | | This is going to setup the required access between our Heroku app and this S3 bucket |
Creating an AWS Account | 11 | Copy the following code into the CORS configuration window | <img width="249" alt="image" src="https://user-images.githubusercontent.com/81588887/165566820-1ae07646-7402-4914-9e15-6a540ad6fea2.png"> |
Creating an AWS Account | 12 | Now go to the bucket policy tab and select policy generator | | This is so we can create a security policy for this bucket |
Creating an AWS Account | 13 | The type of policy is going to be S3 Bucket Policy |
Creating an AWS Account | 14 | We will allow all principals by using an asterisk in the field box |
Creating an AWS Account | 15 | Now copy in the ARN which stands for Amazon resource name from the other tab and paste it into the ARN box at the bottom |
Creating an AWS Account | 16 | Click add statement, then generate policy |
Creating an AWS Account | 17 | Then copy the policy into the bucket policy editor. Before you click save, you want to allow access to all resources in this bucket |
Creating an AWS Account | 18 | Add a `/*` onto the end of the resource key and click save | `/*` |
Creating an AWS Account | 19 | Now go to the access control list tab and set the list objects permissions for everyone under the Public Access section and click save |
Creating AWS Groups, Policies and Users | 1 | Search for IAM in AWS and open it |
Creating AWS Groups, Policies and Users | 2 | Click groups, create a new group and give a name to the group that relates to your heroku app name. Then click next step until there is an option to create group |
Creating AWS Groups, Policies and Users | 3 | Now click on policies and then click create policy |
Creating AWS Groups, Policies and Users | 4 | Go to the JSON tab and then click import managed policies. Search for the S3 full access policy |
Creating AWS Groups, Policies and Users | 5 | Grab the bucket ARN from the bucket policy page in S3 and paste that in the Resource section of the code, placing the asterisk | <img width="391" alt="image" src="https://user-images.githubusercontent.com/81588887/165577696-d859e4e5-5ce5-437b-8dba-6c8dc73f0267.png"> |
Creating AWS Groups, Policies and Users | 6 | Now click review policy, give it a name and a description and then click create policy |
Creating AWS Groups, Policies and Users | 7 | Your policy has now been created
Creating AWS Groups, Policies and Users | 8 | Go to groups, click on your bucket group, click attach policy, search for the policy just created and select it and click attach policy |
Creating AWS Groups, Policies and Users | 9 | Now click on users, click add user, create user named 'heroku_app_name-staticfiles-user' and give them programmatic access, then select next |
Creating AWS Groups, Policies and Users | 10 | Now select the policy you want for the user, click next, then click create user |
Creating AWS Groups, Policies and Users | 11 | Now download the csv file which will contain this users access key and secret access key | | It's very important to download and save this file, because once you have gone past this step, you won't be able to download this file again |
Connecting Django to S3 | 1 | In your terminal install two packages | `pip3 install boto3` and `pip3 install django-storages` |
Connecting Django to S3 | 2 | Now freeze the new packages | `pip3 freeze > requirements.txt` |
Connecting Django to S3 | 3 | In settings.py, add storages to installed apps | `storages`
Connecting Django to S3 | 4 | Scroll down in settings.py to the static files section and copy in the following code | ![image](https://user-images.githubusercontent.com/81588887/165580532-0eced2dd-d142-4e85-94f5-844fdbed0d70.png) |
Connecting Django to S3 | 5 | Go Heroku's website and add the AWS keys to the config variables and set 'USE_AWS' as the key and the value to True |
Connecting Django to S3 | 6 | Now remove 'DISABLE_COLLECTSTATIC' variable | | Django should collect the static files automatically and upload them to S3 |
Connecting Django to S3 | 7 | In Gitpod, create a file called custom storages | | custom_storages.py
Connecting Django to S3 | 8 | inside this file, type the following | ![image](https://user-images.githubusercontent.com/81588887/165581857-848e0e03-53c6-4ced-986e-5f8c01481eac.png) |
Connecting Django to S3 | 9 | Now commit and push these changes to Github |
Connecting Django to S3 | 10 | Now check heroku's activity tab and see if your app is being deployed successfully. You will also see that in your S3 account, you will your static files have been uploaded |
Caching, Media Files & Stripe | 1 | Go to AWS S3 and create a new folder called media | `media` |
Caching, Media Files & Stripe | 2 | Inside the media folder, click upload, add files and select all the images that you need to upload. Then click next |
Caching, Media Files & Stripe | 3 | Under manage public permissions, select grant public read access to these objects, click next until you get to the end and click upload |
Caching, Media Files & Stripe | 4 | Now go to the Django admin and log into the admin panel |
Caching, Media Files & Stripe | 5 | If you don't see your superuser email here, you may need to log in first and force allauth to create it and then come back to admin panel. Once you see your email, simply mark it as verified and primary in the admin |
Caching, Media Files & Stripe | 6 | Now go to stripe.com and login |
Caching, Media Files & Stripe | 7 | Click developers and then API keys |
Caching, Media Files & Stripe | 8 | Copy your public key, go to heroku and add it as a config variable under 'STRIPE_PUBLIC_KEY'. Do the same again for the stripe secret key |
Caching, Media Files & Stripe | 9 | Now create a new webhook endpoint. Go to webhooks, add endpoint, add the url from the heroku app, followed by checkout and wh | `https://homeish.herokuapp.com/checkout/wh/` |
Caching, Media Files & Stripe | 10 | Select to receive all events and click add endpoint |
Caching, Media Files & Stripe | 11 | Now you can see your secret key. Now add the webhook value in the Heroku config var settings with the key name 'STRIPE_WH_SECRET' |
Caching, Media Files & Stripe | 12 | Now send a test webhook from Stripe to make sure that the listener is working | <img width="639" alt="image" src="https://user-images.githubusercontent.com/81588887/165585858-d248b80a-e3ef-4a1b-bfc1-f6929ad10674.png"> |

</details>

## Technologies Used
* HTML5
* CSS3
* JavaScript
* Python3
* Django
* Postgres
* Stripe Payments

## Credits

### Code
* Code Institute tutorial videos
* CSS code for the footer from Colorlib.com
* Responsive image gallery on the homepage from YouTube

### Images
* Unsplash.com
* Made.com

### Content
* Self created content, except for product descriptions, which came from Made.com.

### Acknowledgements
* My mentor Rahul for his ongoing support and feedback
* The Code Institute’s Tutor Support
* The Slack community

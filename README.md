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

* Non logged in users cannot access content that is for logged in users, as the code specifies that the user needs to be logged in to view content `@login_required`. If they attempt to, they will also be redircted to the home page.
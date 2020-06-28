[![Build Status](https://travis-ci.org/IchaTreasure/TGDrums.svg?branch=master)](https://travis-ci.org/IchaTreasure/TGDrums)

<h1>TGDrums</h1>

<h2> WHAT IS IT? </h2>
<hr>
<p> TGDrums is an ecommerce store selling Drum Kits and drum accesories. It was created as a final project of a Code Institute web 
development diploma to display skills learnt over the course. The overall aim is to build a custom built Django project composed 
of multiple apps. TGDrums is a fictional brand using images and content from Different online drum stores. This project was designed to show case 
the products in an appealing way that encourages the customer to browse and make a purchase. The focus is on the user having an 
effortless experience with a design that feels intuitive.</p>

<h2>UX</h2>
<hr>
<p>The web application is designed to be extremely straight forward, a registration page for new users, a login page for existing users which takes them to the homepage.
The homepage has links to All Products which shows all the products that have been added into the database, then another link with a dropdown to 5 different categories i.e 
Acoustic Drum, Electric Drums, Snare Drums, Cymbals, and Drumsticks. When clicking any of this links sends the user to all the products with that category. There is a search form that 
searches the database for any product.
When a user clicks the read more button to view a product they can view the product description and add the product tot the cart if they want. 
</p> 

<h2>Database Design</h2>
<hr>
<img src="/media/images/Database design.jpeg">
<br>

<h2>User Stories</h2>
<hr>
<p>This web application is accesible for all user from mobile device and desktop.</p>

<p> As a new user I'm able to do the following:</p>

<p>• View the Homepage</p>
<hr>
<img src="/media/images/Home pic.jpeg">
<br>

<p>• Register/ Login to use the online shop.</p>
<hr>
<img src="">
<br>
<img src="">
<br>

<p>• Go to the Shop page where all the products will be shown.</p>
<hr>
<img src="/media/images/Shop PIC.jpeg">
<br>

<p>• The user is able to search for a product with the help of the search form on the navbar</p>

<p>• The user is able to see a product description by clicking on the read more botton on the product cards</p>
<hr>
<img src="/media/images/Product PIC.jpeg">
<br>

<p>• The user is able to add a product to the shopping cart</p>
<hr>
<img src="/media/images/cart PIC.jpeg">
<br>

<p>• The user is able to make a payment for a product</p>
<hr>
<img src="/media/images/Checkout PIC.jpeg">
<br>

<h2>Features</h2>
<hr>
<h6>The Register Page</h6>
<p>When a user is not logged in, the register nav item appears in the Nav bar. A user will be able to register, via the register form on the register page. If a user with an account, finds themselves on this page by mistake, they are guided to click "HERE" to direct them to the login page. Within the register form, are fields for email address, Username, Password and Password Confirmation.</p>

<h6>The Login Page</h6>
<p>The login page features a standard login form asking for username and password. It does have the option to reset your password, if you have forgotten it. By clicking on the "I forgot my password" button, the user will be directed to another page where they must input their email address. The user will be emailed a set of instructions of how to reset their password. There is also an option for users that find themselves on this page, that don't have an account. If they click HERE, they get redirected to the register page.</p>

<h6>Shop Page</h6>
<p>Products are displayed on bootstrap cards, each card shows an image of the product and a button that takes the user to the product details, price and input field where the user can select a quantity, clicking the add button will add the product to their shopping cart.</p>

<h6>The 'My Profile' Page</h6>
<p>This option on appears in the nav bar when the user has logged in. once clicked, the user is directed to another page, where the page displays their email address and username.</p>

<h6>The 'MyCart' Page</h6>
<p>The Shopping cart page features a summary of all the items the user has added to their cart. Each Product has a thumbnail picture, to remind the user of their purchase. There is a price value for each product that has been added to the cart. There is also a quantity value, and an option to amend that quantity value. If the user decides they want to remove that product, they must amend the value to zero. The order summary at the bottom give the total amount that all the items come to. Below thisvalue, is the button to "Proceed to checkout". Only users that are logged in, will be able to proceed to the checkout section. Users that are not logged in, and redirected back to the login page.</p>

<h6>Checkout</h6>
<p>The checkout section is quite similar to the cart section, with the main exception that the user is not able to alter their products picked for purchase. If they wish to do so, they can click on the MyCart navbar item. Below the Checkout summary of the total cost, there is the payment section, where the users card details can be entered to purchase the products. Once Submit payment is clicked, the user is directed to the home page, and a message should be displayed to advise the user if their payment was accepted or not.</p>

<h6>Search functionality</h6>
<p>To search for products by name or letters.</p>

<h6>Products by categories</h6>
<p>5 main product categories</p>

<h6>The Footer</h6>
<p>The Footer is on every page, and has been kept clean and simple. Links to External Sites, Social Media links and The company name and caption. Also included at the bottom of the logo is Copyright 2020 & name of the developer.</p>


<h2> Future features </h2>
<hr>
<p>Due to the steeper learning curve of Django and project time constraints, many features that I want to implement 
to make the ecommerce website more complete were left out.</p>
<p>• Profiles: Multiple Addresses, Wishlist, Storing Address in Order Model</p>
<p>The profile app can allow for multiple addresses. Order made to the address should also be stored in the order transaction history, 
or to be more precise, the Order Model. A wishlist feature can be implemented for users to add products they want for future reference.</p>
<p>• Reviews.</p>
<p>• Pagination </p>
<p>• Sending Email for Verification </p>
<p>Discount Codes</p>
<p>Like most online shopping businesses these days, there can be a discount code system that provides various benefits to 
customers such as a price discount or free gifts.
</p>
<p>A wishlist, where the user can pick products and "favorite" them, before deciding to add them to the cart or not. The user can click on the wishlist link and review the products they have favored. This saves time and gives the user a better user experience overall. </p>
<p>A section on the homepage showing the most popular purchased products at that current time. </p>


<h2>Tools/Technologies</h2>
<hr>
<h3>Html</h3>
<p>A standard markup language for documents designed to be displayed in a web browser.</p>

<h3>CSS</h3>
<P>A language that describes the style of a HTML document.</p>

<h3>Python</h3>
<p>A language used on a server to create web applications.</p>

<h3>Google Fonts</h3>
<p>Used to style the fonts of the website.</p>

<h3>jQuery</h3> 
<p> To make certain features function on the page.</p>

<h3>fontawesome</h3>
<p>for social media icons.</p>

<h3> Django </h3> 
<p>A Python-based free and open-source web framework that follows the model-template-view architectural pattern.</p>

<h3>PostgresSQL</h3>
<p>Backend database used to store the information on the products</p>

<h3>Travis-CI</h3> 
<p>Travis CI is a hosted continuous integration service used to build and test software projects hosted at GitHub</p>

<h3>Stripe</h3> 
<p>An API that allows individuals and businesses to make and receive payments over the Internet.</p>

<h3>AWS Cloud9</h3>
<p>Cloud9 hosted my Workspace for this project</p>

<h3>Git</h3>
<p>Used to push and commit any and all changes to my repository on GitHub</p>

<h3>Bootstrap</h3>
<p>Allows for extra responsiveness of html5 and JavaScript files, also Provided my buttons and modal.</p>

<h3>Heroku</h3>
<p>The site has been deployed using Heroku and is available to visit here: https://tgdrums.herokuapp.com/</p>


<h2>Databases</h2>
<hr>
<h3>Databases used</h3>
<hr>
<p>Django normally works with SQL databases and comes prepacked with sqlite3. During development on my local 
machine I worked with the standard sqlite3 database installed with Django. On deployment, the SQL database 
provided by Heroku is a PostgreSQL database.</p>

<h3>Plugins</h3>
<hr>
<p>• https://fonts.googleapis.com/icon?family=Material+Icons</p>
<p>• https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css</p>
<p>• https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js</p>
<p>• https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js</p>
<p>• https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css</p>
<p>• https://use.fontawesome.com/releases/v5.6.1/css/all.css</p>
<p>• https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css</p>
<p>• https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.slim.min.js</p>
<p>• https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.bundle.min.js</p>
<p>• https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css</p>
<p>• https://cdnjs.cloudflare.com/ajax/libs/hover.css/2.3.1/css/hover-min.css</p>

<h3>Testing</h3>
<hr>
<h6>User Testing</h6>
<p>Manual User testing:</p>
<hr>
<p>This was the primary method of testing the application. People were asked to visit the website on a variety of devices, 
to setup accounts within the web store and to purchase items in the store. This feedback was very useful to determine 
any bugs that may have been present. I also tested the app manually myself on a varietly of browsers.</p>

<h6>Below are the list of Internet Browsers that were used to test the display of the website:</h6>
<hr>
<p>• Google Chrome (Version 77.0)</p>
<p>• Mozilla Firefox</p>
<p>• Microsoft Edge</p>
<p>• Internet Explorer 11</p>

<h6>Below are the list of websites I used to test the HTML, CSS, JS and Python code:</h6>
<hr>
<p>• The HTML and CSS coding was tested by using the W3C Mark Validator Service by direct input.</p>
<p>• To test the responsiveness of the website in phones, tablets, and desktops screens, I have used the Chrome Developer Tools.</p>
<p>• The JavaScript files were tested using https://jslint.com/ by direct input of the files on the validator.</p>
<p>• The Python code tested on pep8 </p>

<h5>Individual Page Testing:<h5>
<hr>
<h6>Home/Index</h6>
<p>The user clicked on registration and filled out the registration form before 
logging out and back in again to test that login was also working. The user also clicked on all navbar tabs to ensure each page 
loaded as expected and clicked on the 'Shop Now' button to check it redirected as intended. All colour and text is consistent, 
all elements are aligned correctly. </p>

<h6>Shop</h6>
<p>Database is connected and all products are displayed with the correct information. Adding a product updated the cart as intended. 
All colour and text is consistent, all elements are aligned correctly. Page was tested for responsiveness and behaved as expected.</p>

<h6>Cart</h6>
<p>Cart displayed all products added during the shop process. Quantity amend was increased and decreased to check that each item updated 
correctly which they did. The Checkout button was also checked to ensure it redirected correctly and behaved as expected. All colour and 
text is consistant, all all elements are aligned correctly. Page was tested for responsiveness and behaved as expected. </p>

<h6>Checkout</h6>
<p>The form was filled out using a dummy credit card number to ensure the Stripe payment was processed. The database 
was then checked and all cart items were deleted as expected and the stripe developers website showed that the payment had gone through 
successfully. All colour and text is consistent, all elements are aligned correctly. Page was tested for responsiveness and behaved as expected. </p>

<h5>Automated testing</h5>
<hr>
<p>The unittest framework built into Django was used for testing some modules in each app and running the coverage report 
to get a detailed report of how well each Django module was tested. Where I was not able to automate tests for that particular module I 
used manually testing thoroughly to ensure my app was tested throughout.</p>

<p>Travis CI was implemented to help continuously test my app through the development process. You can click the 'build passing' icon at the top 
of my repo to check out Travis on this app.</p>

<h2>Bugs</h2>
<hr>
<p>Had some issues with adding reviews</p>

<h2>Deployment</h2>
<h4> Creating a requirements.txt and Procfile</h4>
<p>• In CLI input pip3 freeze --local > requirements.txt . This should generate a file with all tools listed and they're version number.</p>
<p>• Procfile - in CLI input echo web: gunicorn tgdrums.wsgi:application > Procfile</p>
<h4> Creating an app on Heroku</h4>
<p>• Create account with Heroku.</p>
<p>• Select "New" then "Create new app"</p>
<p>• Input app-name and region (Europe in this case)</p>
<p>• Follow steps for "Deploy using Heroku Git" (push from CLI, described below)</p>
<p>• Set Config vars (described below)
<h4> Push to Heroku </h4>
<p>• First, ensure requirements.txt and Procfile are configured.</p>
<p>• In temrinal window, run "heroku login"
<p>• Press and key to be redirected to Heroku Login page, select "Login in to Heroku CLI"</p>
<p>• Return back to Terminal, Heroku should be logged in, run the command "git push heroku master".</p>

<h4> Set config vars on Heroku</h4>
<p>• From your app dashboard, select settings</p>
<p>• In settings, select "Reveal config vars"</p>

<p>The repository can be found on: https://github.com/IchaTreasure/TGDrums</p>

<p>The site has been deployed using GitHub Pages and is available to visit here: http://tgdrums.herokuapp.com/</p>

<h2>Credits</h2>
<p>I would to credit the following sources for their inspiration:</p> 
<p>Stack Overflow community</p>
<p>CodePen community </p>
<p>GitHub community</p> 
<p>W3schools</p>

<h2>Media</h2>
<p>Images were taken from google.</p> 

<h2>Acknowledgement</h2>
<p>I would like to thank my mentor Anthony Ngene, for his support throughout this project.</p>

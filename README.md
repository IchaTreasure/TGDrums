
[![Build Status](https://travis-ci.org/IchaTreasure/TGDrums.svg?branch=master)](https://travis-ci.org/IchaTreasure/TGDrums)

<h1>TGDrums</h1>

<h2> WHAT IS IT? </h2>

<p> TGDrums is an ecommerce store selling Drum Kits and drum accesories. It was created as a final project of a Code Institute web 
development diploma to display skills learnt over the course. The overall aim is to build a custom built Django project composed 
of multiple apps. TGDrums is a fictional brand using images and content from Different online drum stores. This project was designed to show case 
the products in an appealing way that encourages the customer to browse and make a purchase. The focus is on the user having an 
effortless experience with a design that feels intuitive.</p>

<h2>UX</h2>
<p>The web application is designed to be extremely straight forward, a registration page for new users, a login page for existing users which takes them to the homepage.
The homepage has links to All Products which shows all the products that have been added into the database, then another link with a dropdown to 5 different categories i.e 
Acoustic Drum, Electric Drums, Snare Drums, Cymbals, and Drumsticks. When clicking any of this links sends the user to all the products with that category. There is a search form that 
searches the database for any product.
When a user clicks the read more button to view a product they can view the product description and add the product tot the cart if they want. 
</p> 


<h2>Database Design</h2>
<img src="/media/images/Database design.jpeg">
<br>

<h2>User Stories</h2>
<h6>This web application is accesible for all user from mobile device and desktop.</h6>

<h6> As a new user I'm able to do the following:</h6>

<h6>• View the Homepage</h6>
<img src="/media/images/Home pic.jpeg">
<br>

<h6>• Register/ Login to use the online shop.</h6>
<img src="">
<br>
<img src="">
<br>

<h6>• Go to the Shop page where all the products will be shown.</h6>
<img src="/media/images/Shop PIC.jpeg">
<br>

<h6>• The user is able to search for a product with the help of the search form on the navbar</h6>

<h6>• The user is able to see a product description by clicking on the read more botton on the product cards</h6>
<img src="/media/images/Product PIC.jpeg">
<br>

<h6>• The user is able to add a product to the shopping cart</h6>
<img src="/media/images/cart PIC.jpeg">
<br>

<h6>• The user is able to make a payment for a product</h6>
<img src="/media/images/Checkout PIC.jpeg">
<br>


<h2>Features</h2>
<p>• User Registration: User's who wish to buy products will have to register first. </p>
<p>• User Login: Registered users must login before attempting to but any product from the online store.</p>
<p>• Messages indicating if Username is already taken at registration, or incorrect username/password at login.</p>
<p>• User Logout: Enables the user to end the session.</p>
<p>• Search functionality: To search for products by name.</p>
<p>• Products by categories: 5 main product categories</p>

<h2> Future features </h2>
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


<h2>Tools/Technologies</h2>
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
<h3>Databases used</h3>
<p>Django normally works with SQL databases and comes prepacked with sqlite3. During development on my local 
machine I worked with the standard sqlite3 database installed with Django. On deployment, the SQL database 
provided by Heroku is a PostgreSQL database.</p>

<h3>Plugins</h3>
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
<p>• The HTML and CSS coding was tested by using the W3C Mark Validator Service by direct input.</p>
<p>• To test the responsiveness of the website in phones, tablets, and desktops screens, I have used the Chrome Developer Tools.</p>
<p>• The JavaScript files were tested using https://jslint.com/ by direct input of the files on the validator.</p>
<p>• The Python code tested on pep8 </p>
<p>• The web app functionality, tested on multiple browers such as Chrome, Edge, Safari and Firefox.</p>
<p>• The web application has been tested by some of my friends with the question if the app was clear, easy to use and understandable.</p>

<h2>Bugs</h2>
<hr>
<p>Had some issues with adding reviews</p>

<h2>Deployment</h2>
<hr>
<h4>Modules to be installed</h4>
<p>• os</p>

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


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


<h2>User Stories</h2>
<p>This web application is accesible for all user from mobile device and desktop.</p>

<p> As a new user I'm able to do the following:</p>

<p>• Register/ Login to use the online shop.</p>
<img src="">
<br>
<img src="">
<br>

<p>• Go to the Shop page where all the products will be shown.</p>
<img src="">
<br>

<p>• The user is able to search for a product with the help of the search form on the navbar</p>
<p>• The user is able to see a product description by clicking on the read more botton on the product cards</p>


<h2>Features</h2>
<p>• User Registration: User's who wish to buy products will have to register first. </p>
<p>• User Login: Registered users must login before attempting to but any product from the online store.</p>
<p>• Messages indicating if Username is already taken at registration, or incorrect username/password at login.</p>
<p>• User Logout: Enables the user to end the session.</p>
<p>• Search functionality: To search for products by name.</p>
<p>• Products by categories: 5 main product categories</p>

<h2> Future features </h2>
<p>• Comments section: Give other users the ability to comment/critique on others work.</p>
<p>• Rate recipes: Rate the recipes with a star rating system.</p>
<p>• Add pictures </p>

<h2>Tools/Technologies</h2>
<h3>AWS Cloud9</h3>
<p>Cloud9 hosted my Workspace for this project</p>

<h3>Git</h3>
<p>Used to push and commit any and all changes to my repository on GitHub</p>

<h3>Bootstrap</h3>
<p>Allows for extra responsiveness of html5 and JavaScript files, also Provided my buttons and modal.</p>

<h3>JavaScript</h3>
<p>JavaScript has been used to implement the functionalities of the nav, slider and nav dropdown</p>

<h3>Heroku</h3>
<p>The site has been deployed using Heroku and is available to visit here: https://tgdrums.herokuapp.com/</p>

<h3>Plugins</h3>
<p>• https://fonts.googleapis.com/icon?family=Material+Icons</p>

<p>• https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css</p>

<p>• https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js</p>

<p>• https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js</p>

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
<p>Had some issues with adding pictures into s3 bucket and calling the files into my html pages</p>

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

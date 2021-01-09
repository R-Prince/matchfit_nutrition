# MatchFit Nutrition

An online cookbook that allows users to share and easily access recipes that will help to fuel their training sessions and matches. Like the name suggests MatchFit Nutrition will provide tried and tested recipes for athletes that are easy to follow and hopefully taste delicious. This website also features tips on nutrition from some of the worlds leading sport nutritionists to inspire athletes and increase the importance of nutrition and how it can improve performance. 

Whether the user is an amateur, semi-professional or professional athlete they will be able to share their recipes with the community and access recipes with the goal of ultimately helping to improve nutrition and performance. Expert advice from top sport nutritionists will also be presented to the user in the form of blogs to help improve nutrition no matter the level they are playing at. 

![preview](/readme/images/preview.png)

[MatchFit Nutrition](https://matchfit-nutrition.herokuapp.com/)

Business goals: 
- Provide recipe and tips to help improve athlete nutrition and performance.
- Promote awareness and importance of nutrition in sport.
- Promote awareness of selected sport nutritionists.

User goals:
- Easily find recipes to help improve nutrition and performance.
- Share recipes to help other athletes improve nutrition and performance.
- Find more information on nutrition and how it can improve performance. 

# Table of Contents
1. [UX](#UX)
2. [Features](#Features)
3. [Features Left to Implement](#Features-left-to-Implement)
4. [Information Architecture](#Information-Architecture)
5. [Technologies Used](#Technologies-Used)
6. [Testing](#Testing)
7. [Deployment](#Deployment)
8. [Heroku Deployment](#Heroku-Deployment)
9. [Credits](#Credits)

# UX

#### Ideal Client

The ideal client for this business is: 
- Someone who plays sport.
- Over 16 years old.
- Interested in cooking. 
- Interested in sport nutrition. 
- Interested in health and fitness.

Visitors to this website are searching for: 
- Healthy recipes that are great for athletes.
- Breakfast, Lunch and Dinner options. 
- Nutrition tips that will help improve performance.
- Platform to easily share recipes. 

This website helps users achieve this goal by:
- Providing easy to follow recipes for athletes. 
- Search function so users are able to easily search for recipes. 
- Blog posts from sport nutritionists. 
- Easy fillable forms so users can share recipes. 

### Clients stories
1. As a new visitor to the website or registered user, I want to easily be able to view recipes. 
2. As a new visitor to the website or registered user, I want to be able to view ingredients and instructions that are clear and easy to follow.
3. As a new visitor to the website or registered user, I want to easily view tips on sports nutrition. 
4. As a new visitor to the website , I want to easily sign up to the site and share recipes. 
5. As a new visitor to the website or registered user, I want to easily search for new recipes. 
6. As a registered user, I want to easily add recipes to the site.
7. As a registered user, I want to easily edit and delete recipes I have shared. 

### Wireframes
These wirerames were created using [Balsamiq](https://balsamiq.com/) during the planning process for the project and includes wireframes for desktop, tablets and mobile devices.

[MatchFit Nutrition Wireframes](/readme/wireframes/MatchFitWireframes.pdf)

# Features

### Navigation Bar 
The navigation bar includes the MatchFit Nutrition logo in the top left corner. 

- For visitors that are not logged in, the below links are available:
    1. Home
    2. Recipes
    3. Blog
    4. Log In 
    5. Register

- For users that are logged in, the below links are available:
    1. Home
    2. Recipes
    3. Blog
    4. Add Recipe
    5. Profile 
    6. Log Out

The navigation bar will display the different links depending on if the “user” is in session which is determined using a Jinja if statement. 

The navbar collapses into a hamburger icon on the top left corner on tablet and mobile devices. The MatchFit Nutrition logo is then moved to the centre of the navbar. On small mobile devices the logo only displays MatchFit. 

The side navbar includes the same links as above but also includes a Matchfit logo at the top of the page. 

## Homepage (Index)

Hero Section:

The hero section includes a video playing in the background of a hot plate of potatoes in a bowl. This videos lasts around 4 seconds and is played on a constant loop. This video is displayed on all screen sizes. In front of the video is the name of the site and a tagline for the website. Directly underneath is a call to action button “View Recipes” which directs the users to recipe page which is one of the main features of the website. 

Feature Section:

The feature section includes the 3 main benefits of the website and is used so that the user can easily navigate and access the users goals. Each feature displays an icon related to the benefit, a brief description and a call to action button. 
1. Fuel your performance (view recipes)
2. Share your favourite recipes (Register now)
3. Top tips from Sport Nutritionists (view blog)

On large and medium screens the features are display in one row but on smaller devices each feature is stacked and has it’s own row. 

Latest Recipes Section:

This section includes 3 of the latest recipes created on the website by users. These are listed in order using python and are sorted by the date on which these were created. Each recipe card includes a picture of the recipe(if available or a generic image is used), name of the recipe, a brief description of the recipe, which category it falls under (Breakfast, Lunch, Dinner), how long it takes to make the recipe in minutes and the difficult of the recipe (Easy, Moderate or Hard). The footer of the card also includes a call to action button “View Recipe” which will direct the user to the full recipe. 3 recipe cards were used for this section to give the user a taste of what kind of recipes are available on the site.

On larger screen sizes the cards are displayed in landscape mode which includes the image on the left and then the details of the recipe alongside the image in a row. On tablet and mobile devices the cards are displayed in portrait mode where the image is displayed on top and directly underneath the details of the recipe. 

About Section:

This section includes a paragraph which outlines the aims of Matchfit Nutrition and why it was created. This gives the user an idea of what they can expect using this website and what they are trying to achieve. Below the paragraph includes an downward arrow which prompt the user to scroll down to the next section which is the latest blog where they can see the latest blog written on sport nutrition. 

Latest Blog Section:

This section includes a card detailing the latest blog written on the site. This cars is selected using python and is sorted by the date on which the blog was created. The card includes an image related to the blog (if available or a generic image is used), title of the blog, a brief description of the blog, read time in minutes and who was the author of the blog. The footer of the card also includes a call to action button “Read Blog” which will direct the user to the full blog. The cards are displayed in the same manor as the recipe cards to keep consistency across the site. This includes the same layout for desktop, tablets and mobile devices. 

Footer:

The footer includes MatchFit Nutrition header with a tagline. It also includes a Social Media header with links to all the Matchfit social media which includes Facebook, Twitter, Instagram and Pinterest. On smaller screens and mobile devices the footer is stacked and the social media links are underneath  the footer header and tagline. 

## Recipe page

The recipe page  displays all the recipes created in the database along with a search feature that allows users to search for a recipe using key words. Users can also filter the recipes by categories (Breakfast, Lunch and Dinner). 

After the page header the search bar is displayed which allows users to easily search for recipes via ingredients, category or words in the recipe title. Directly underneath the search bar is two buttons. “Search” button is used to submit the data in the search bar and the “cancel” button is used to reset and cancel the current word being searched. 

Below the search feature is three checkboxes that allow users to filter recipes by category (Breakfast, Lunch and Dinner). Once a user selects a checkbox the box is checked and results relating to that category are shown to the user. 

Both search functions also include “No recipe found!” message for searches that return no results. 

Below the search function are the recipe cards which shows all the recipes in the database. These are listed in order using python and are sorted by the date on which these were created. Each recipe card includes a picture of the recipe(if available or a generic image is used), name of the recipe, a brief description of the recipe, which category it falls under (Breakfast, Lunch, Dinner), how long it takes to make the recipe in minutes and the difficult of the recipe (Easy, Moderate or Hard). The footer of the card also includes a call to action button “View Recipe” which will direct the user to the full recipe. 3 recipe cards were used for this section to give the user a taste of what kind of recipes are available on the site.

On larger screen sizes the cards are displayed in landscape mode which includes the image on the left and then the details of the recipe alongside the image in a row. On tablet and mobile devices the cards are displayed in portrait mode where the image is displayed on top and directly underneath the details of the recipe.

The last feature on this page before the footer is a call to action button “Back to Recipes” which directs the user back to the top of the page and resets the search function to show all recipes. 

## Blog Page

The blog page displays all the blogs created in the database using cards. The cards includes an image related to the blog (if available or a generic image is used), title of the blog, a brief description of the blog, read time in minutes and who was the author of the blog. The footer of the card also includes a call to action button “Read Blog” which will direct the user to the full blog. The cards are displayed in the same manor as the recipe cards to keep consistency across the site. This includes the same layout for desktop, tablets and mobile devices. 

## Add Recipe Page 

The add recipe page includes a form that allows user to create new recipes. This page is only available to registered users that are logged in. The form is shown in a card which includes fields listed below: 
1. Recipe name
2. Brief description of recipe
3. Recipe Category - Dropdown field including: Breakfast, Lunch and Dinner 
4. Recipe Difficulty - Dropdown field including: Easy, Moderate and Difficult  
5. Recipe Duration 
6. Ingredients (This field includes a button directly underneath that allows the user to add another ingredient field to the form. The newly added field has an icon “rubbish bin” which allows users to delete the field that was just created. At least one ingredient is needed to submit the form)
7. Recipe method (Similar to the ingredient field it includes a button directly underneath that allows the user to add another recipe method field to the form. The newly added field has an icon “rubbish bin” which allows users to delete the field that was just created. At least one recipe method is needed to submit the form)
8. Add image link (This allows users to supply a link to an image of the recipe. If the link is broken or not supplied a generic image is used for the recipe)

Every field is required to submit the form except the “Add image link” field. Each field that is required has a validating function which will turn the input field red if not filled out correctly or green if the field is filled out correctly. That includes the Recipe name and description being at least 3 characters long. For the recipe duration an integer must be submitted. 

Below the input fields are two buttons. The “Add Recipe” button submits the form and creates the recipe on the site. The “Cancel” button stops the form from being submitted and redirects the user to the recipe page. 

The last feature on this page before the footer is a call to action button “Back to Recipes” which directs the user back to the recipe page. 

## Edit Recipe Page

The edit recipe page is similar to the “add recipe” page and includes the same input fields. The only difference is the input fields are already filled with what the user has already inputted into the database for this recipe. The user is then able to make any changes to the recipe by editing the data in the input fields. 

Below the input fields are two buttons. The “Submit Changes” button submits the form and updates the recipe on the site. The “Cancel” button stops the form from being submitted and redirects the user to the recipe page. 

Users will only be able to edit their own recipes which is identified using their “session” cookie. The link to this page is supplied on the profile page or when they are viewing the recipe on the website. 

On smaller devices where the card is in portrait mode a “edit” icon is displayed  on the title of the card. On viewing the recipe page a floating action button is displayed in the bottom right corner which when hovered reveals the edit button. 

## Delete Recipe Button

The delete recipe button is available on the profile page or when they are viewing the recipe on the website. On smaller devices where the card is in portrait mode a “rubbish bin” icon is displayed  on the footer of the card. On viewing the recipe page a floating action button is displayed in the bottom right corner which when hovered reveals the delete button. 

When a user clicks on the delete button a modal page will pop up confirming if the user would like to delete the recipe. This is to stop users accidentally deleting the recipe from the website. 

## Show Recipe Page

The show recipe page allows users to view all the details for the recipe including ingredients and the method to making the recipe. After the page header which displays the recipe name a picture of the recipe is shown. If no picture is supplied or the link is broken then a generic image is used instead. Directly below the image is a brief description of the recipe. Followed by the duration and difficulty of the recipe aligned to the left hand side. 

The ingredients and method is then displayed in a row. The ingredients take up 4 columns of the row and the ingredients are then displayed in an unordered list. The Recipe method then take up the remaining 8 columns in the row and the recipe methods are then displayed in an ordered list. On smaller screen sizes each section takes up one row, the ingredients are displayed first followed by the recipe method. 

Directly below the row including the ingredients and method is information on who created the recipe slightly aligned to the right. 

## Add Blog Page 

The add blog page includes a form that allows the site owner/admin to create a new blog article. This page is only available to admin user once they have logged in. The form is shown in a card which includes fields listed below: 
1. Blog title (Minimum 3 characters)*Required 
2. Blog preview (Minimum 3 characters)*Required 
3. Blog Author (Minimum 3 characters)*Required 
4. Read Time (Must be supply an integer)*Required 
5. Blog Text (Tiny MCE rich text editor is used for this field)*Required 
6. Add Image Link (This allows users to supply a link to an image that represents the blog. If the link is broken or not supplied a generic image is used for the blog)

Each field that is required has a validating function which will turn the input field red if not filled out correctly or green if the field is filled out correctly. The blog test feature also includes a modal that instructs the user that this field cannot be left empty. 

Below the input fields are two buttons. The “Add Blog” button submits the form and creates the blog on the site. The “Cancel” button stops the form from being submitted and redirects the user to the blog page. 

The link to this page is supplied on the profile page and is only available to the admin user of this site. 

## Edit Blog Page

The edit blog page is similar to the “add blog” page and includes the same input fields. The only difference is the input fields are already filled with what the user has already inputted into the database for this blog. The user is then able to make any changes to the blog by editing the data in the input fields. 

Below the input fields are two buttons. The “Update Blog” button submits the form and updates the blog on the site. The “Cancel” button stops the form from being submitted and redirects the user to the blog page. 

Admin users will only be able to edit the blog which is identified using their “session” cookie. The link to this page is supplied on the profile page or when they are viewing the blog on the website. 

On smaller devices where the card is in portrait mode a “edit” icon is displayed  on the title of the card. On viewing the blog page a floating action button is displayed in the bottom right corner which when hovered reveals the edit button. 

## Delete Blog Button 

The delete blog button is available on the profile page or when they are viewing the blog on the website. On smaller devices where the card is in portrait mode a “rubbish bin” icon is displayed  on the footer of the card. On viewing the blog page a floating action button is displayed in the bottom right corner which when hovered reveals the delete button. 

When a user clicks on the delete button a modal page will pop up confirming if the user would like to delete the blog. This is to stop users accidentally deleting the blog from the website. 

## Show Blog Page

The show blog page allows users to view all the details for the blog . After the page header which displays the blog title a picture of the blog is shown. If no picture is supplied or the link is broken then a generic image is used instead. Directly below the image is a preview of the blog. Followed by the read time in minutes and the author of the blog aligned to the left hand side. 

The context of the blog is then displayed in a row. The last feature on this page before the footer is a call to action button “Back to Blog” which directs the user back to the blog page. 

## Profile Page 

The profile page is used to display the users information including Username, First and Last name as well as any recipes or blogs they have added to the site. This page is used so users can view what they have created on the site and edit or delete the content. 

After the page header “MatchFit Nutrition Member” a card is displayed below aligned to the left hand side which details the username, first and last name. The footer of the card also includes three buttons:
1. Logout
2. Add Recipe 
3. Add blog (only displayed on the usernames that include "matchfit")

Only users that have "matchfit" in their username will be abled to access the options to adding and editing blog posts. This was implemented with the idea of only giving access to employees and carefully selected memembers. 
If a user with matchfit in their username is logged in then a blog post section will displayed showing cards with all the different blogs available on the site. Each blog card is displayed in same way which is used throughout the website. However there is also two call to action buttons in the footer “Edit” and “Delete” which allows the user to either delete or edit the blog. 

Directly underneath the blog section if the “admin” user or below the profile card the recipe selection is displayed which displays all the recipes that the user has created on the site. Each recipe card is displayed in the same way as the cards throughout the site. However there is also two call to action buttons in the footer “Edit” and “Delete” which allows the user to either delete or edit the recipe. 

## Login Page

The login page allows users to log into their profile. After the page header “Log In” a form is displayed below in a card with input fields:
1. Username
2. Password

The username and password must match the data in the database for the user to log in. One the user logs in a session cookie is created which allows them to access their recipes and features such as adding a recipe to the site. 

Below the input fields is a button “Login” which submits the form. 

At the bottom of the card is a link for site visitors to register who have visited the site and login page but have not registered yet. 

## Logout Button

This button allows the user to log out of their profile which simply deletes the session cookie created when the user logged into their account. The logout button/link is only available if a user is logged into their account. 

## Register 

The register page allows site visitors to create a profile. After the page header “Register”  a form is displayed below in a card with input fields:
1. First name
2. Last name
3. Username
4. Password

The password is then hashed and kept a secret in the database. A session cookie is then created which allows the user to access new links in the navbar and features such as adding a recipe to the site. 

Below the input fields is a button “Register” which submits the form. 

At the bottom of the card is a link for users to login if they already have an account. 

## Flash Messages 

Flash messages are used to add responses to user input and make them aware or confirm an action they have just made. Flash messages are displayed in a card at the top of each page after the navigation bar. Flash messages include: 
1. Registration Successful 
2. Incorrect Username and/or Password
3. You successfully logged out 
4. Recipe Successfully Added
5. Recipe Successfully Updated 
6. Recipe Successfully Deleted
7. Blog Successfully Added 
8. Blog Successfully Updated 
9. Blog Successfully Deleted 

# Features left to Implement

1. Confirm password - Add an extra field to the register page which required new users to confirm their password when creating a profile. This will avoid any accidental typos when creating a password.
2. Allow certain usernames access to the create a blog button - At the moment only the site admin is allowed to create a blog post on the website. I would like to add a feature that allows certain users to create blog posts e.g Qualified Sport Nutritionists. 
3. Contact Page - A contact would be used to allow site visitors and users to contact MatchFit nutrition if they have any questions. For the time being users can get in contact via social media. 
4. Meal Plan Service - Add a meal plan service where users can subscribe to a meal plan provided by the Matchfit nutrition team. 
5. Like Button - Add a like button to the recipe and blog cards which allow users to rate the recipe or blog. 
6. Search for recipes via username - This would help to promote certain usernames. Users may also like a certain recipe method/style by a user which would make it easier for them to find  the recipes.   

# Information Architecture

MongoDB Atlas database was used this for this project which is a NoSQL database.

### Data Storage Types

- ObjectId
- String
- DateTime
- Array
- Integer

### ERD Diagram

![erd_diagram](/readme/images/erd_diagram.png)

### Collections Data Structure

This website relies on three database collections: 

#### Blogs 

| Title | Key in DB | Form Validation Type | Data Type |
| ------|-----------| ---------------------| ----------|
| Blog ID| _id| None| ObjectId|
| Blog Title| blog_title| minlength="3", text| String|
| Blog Description| blog_description | minlength="3", text| String|
| Blog Image| blog_image| text | String|
| Blog Time| blog_time | number | Integer|
| Blog Author | blog_author| text| String|
| Blog Text| blog_text| minlength="3", text| String|
| Date Created | date_created | None| Date|

#### Recipes

| Title | Key in DB | Form Validation Type | Data Type |
| ------|-----------| ---------------------| ----------|
| Recipe ID| _id| None| ObjectId|
| Recipe Name| recipe_name|minlength="3", text| String|
| Recipe Description | recipe_description | minlength="3", text| String|
| Recipe Time | recipe_time| number | Int32|
| Recipe Difficulty| recipe_difficulty| Dropdown selection, text | String|
| Recipe Category| category| Dropdown selection, text | String|
| Recipe Ingredients| recipe_ingredients| minlength="3", text| Array|
| Recipe Method| recipe_method| minlength="3", text| Array|
| Recipe Image| recipe_image| text | String|
| Date Created | date_created | None| Date|
| Created By | created_by | None | String |

#### Users

| Title | Key in DB | Form Validation Type | Data Type |
| ------|-----------| ---------------------| ----------|
| User ID| _id| None| ObjectId|
| First Name | first_name | text| String |
| Last Name | last_name | text | String |
| Username | username | minlength="5" maxlength="15", text| String |
| Password | password | minlength="5" maxlength="15", text | String |

# Technologies Used 

### Tools 

- [Gitpod](https://www.gitpod.io/) - IDE used to develop this project.
- [Github](https://github.com/) - Store and share all project code remotely.
- [PIP](https://pypi.org/project/pip/) - Used to install tools needed for this project.
- [MongoDB](https://www.mongodb.com/1) - Database used for this project.
- [TinyMCE](https://www.tiny.cloud/)  - Used to create the rich-text editor when creating a blog.

### Libraries 

- [JQuery](https://jquery.com/) - Used for DOM manipulation. 
- [Materialize](https://materializecss.com/) - Used to create the structure and UI for the website and make the website responsive.
- [Font Awesome](https://fontawesome.com/) - Used to provide icons for the website. 
- [Google Fonts](https://fonts.google.com/) - Used to style the website fonts. 
- [Pymongo](https://pymongo.readthedocs.io/en/stable/) - Used to communicate between Python and MongoDB.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)  - Used to construct and render pages. 
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - Used to display data from the backend effectively in the frontend html. 

### Languages
This project uses HTML, CSS, Javascript and Python to programme the website. 

# Testing 

Testing information can be found in a seperate [Testing](readme/testing/testing.md) file.

# Deployment 

###  How to run this project locally

You must have the following tools installed to run this project:

- An IDE such as Gitpod
- Git
- PIP
- Python 3
- MongoD Atlas account 

#### Instructions

1. Follow this link to the [MatchFit Nutrition](https://github.com/R-Prince/matchfit_nutrition) repository.
2. Select the green button which has the options to "clone or download".
3. Copy the "Clone with HTTPS" link.
4. Switch the current working directory to the location where you want to clone the repository.
5. Use command "git clone" followed by pasting the "Clone with HTTPS" link.
6. Create and activate a virtual python environment.
7. Install requirements needed for this project using the command “pip -r requirements.txt”.
8. You will then need to create a env file to create a secret_key and a mongo_uri to link your MongoDB database. Please see [Env sample file](readme/sample_env.txt) for a sample env file. Remember not to upload this file to your repository.
9. Within your database you’ll need to create three collections Blogs, Recipes and Users. Please see “Information Architecture” section for more information the key values created. 
10. Finally you can run now run the application with the command “python3 app.py”.

# Heroku Deployment

To deploy this project to Heroku, please use the following steps:

1. Ensure you have an updated requirements.txt file. If you do not have this file you can create one using the following command “pip freeze > requirements.txt”.
2. Create a Procfile using the command “echo web: python app.py > Procfile”
3. Add and commit the new Requirements and Procfile and push the latest application GitHub. 
4. Create a new app on the Heroku website. 
5. Once on the dashboard for your new Heroku app click on “Deploy” then “Deployment Method” and click GitHub.
6. Select the correct project to and link the heroku app with the GitHub repository. 
7. Back on the dashboard select “Settings” and click on “Reveal Config Vars” and add the following info:

    | Key | Value |
    | ---|---|
    | DEBUG|False|
    | IP|0.0.0.0|
    | PORT|5000|
    | SECRET_KEY|Add your secret key here|
    | MONGO_URI|Add your mongo uri here|

8. Back on the dashboard, click on “Deploy” and ensure the “master” branch is selected. You can then go ahead and click on the “Deploy Branch”. 

# Credits

### Content
- The text used for the recipes were copied from [Mens Health](https://www.menshealth.com/), [Beauty Bites](https://www.beautybites.org/), [Jamie Oliver](https://www.jamieoliver.com/) and [Taste of Home]( https://www.tasteofhome.com/).
- The text used for the blogs were copied from [MaxiMuscle]( https://www.maximuscle.com/) and [MyProtein](https://www.myprotein.com/).

### Media
- All images for the site were obtained from [Unsplash](https://unsplash.com/).

### Acknowledgements
- I received inspiration for this project from a number of different websites:
    - [FourFourTwo](https://www.fourfourtwo.com/performance)
    - [Tasty](https://tasty.co/)
    - [BBC Recipes](https://www.bbc.co.uk/food/recipes)
    - [MatchFit](https://www.matchfitconditioning.com/)


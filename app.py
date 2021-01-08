import os
from flask import (
    Flask, flash, render_template,
    redirect, session, url_for,
    request)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from datetime import datetime
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


def change_date_format(list_data):
    """ Covert datetime format in db into string
    so the date is easier to read """
    modified_dates = []
    for date in list_data:
        date["date_created"] = date["date_created"].strftime("%b %d %Y")
        modified_dates.append(date)
    return modified_dates


@app.route("/")
@app.route("/home")
def home():
    """ Retrieve recipes and blogs from db and return on Homepage """
    recipes = list(mongo.db.recipes.find().limit(3).sort("date_created", -1))
    edited_recipes = change_date_format(recipes)
    blogs = list(mongo.db.blogs.find().limit(1).sort("date_created", -1))
    edited_blogs = change_date_format(blogs)
    return render_template(
        "index.html", recipes=edited_recipes, blogs=edited_blogs)


@app.route("/register", methods=["GET", "POST"])
def register():
    """ Create username in db and use as session cookie """
    if request.method == "POST":
        # Check if username exists in db
        exisiting_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if exisiting_user:
            flash("Username already exists! Please try again")
            return redirect(url_for("register"))

        register = {
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(
                request.form.get("password").lower())
        }
        mongo.db.users.insert_one(register)

        # Create Session cookie for new user
        session['user'] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session['user']))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """ Allow users to log into their profile """
    if request.method == "POST":
        # Check if username exists in db
        exisiting_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if exisiting_user:
            # Ensure password is correct
            if check_password_hash(
                exisiting_user["password"], request.form.get(
                    "password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for("profile", username=session['user']))
            else:
                # Wrong password
                flash("Incorrect Username and/or password")
                return redirect(url_for("login"))
        else:
            # Username doesn't exsist
            flash("Incorrect Username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """ Retrieve recipes and blogs from db and return on Profile Page """
    username = mongo.db.users.find_one(
        {"username": session['user']})
    recipes = list(mongo.db.recipes.find().sort("date_created", -1))
    blogs = list(mongo.db.blogs.find())
    # Redirect user to profile page
    if session["user"]:
        return render_template(
            "profile.html", username=username, recipes=recipes, blogs=blogs)
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """ Clear session cookie and log user out of profile """
    session.clear()
    flash("Your have successfully logged out")
    return redirect(url_for("login"))


@app.route("/recipes")
def recipes():
    """ Retrieve recipes from db and return on Recipe page """
    recipes = list(mongo.db.recipes.find().sort("date_created", -1))
    edited_recipes = change_date_format(recipes)
    return render_template("recipes.html", recipes=edited_recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    """ Search db for recipes and return response """
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    edited_recipes = change_date_format(recipes)
    return render_template("recipes.html", recipes=edited_recipes, query=query)


@app.route("/category", methods=["GET", "POST"])
def category():
    """ Search db for recipes based on category and return response """
    category = request.form.get("category")
    if category:
        recipes = list(mongo.db.recipes.find({"$text": {"$search": category}}))
        edited_recipes = change_date_format(recipes)
        return render_template(
            "recipes.html", recipes=edited_recipes, category=category)
    else:
        return redirect(url_for("recipes"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """ Create new recipe in db """
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_time": int(request.form.get("recipe_time")),
            "recipe_difficulty": request.form.get("recipe_difficulty"),
            "category": request.form.get("recipe_category"),
            "recipe_ingredients": request.form.getlist("recipe_ingredient[]"),
            "recipe_method": request.form.getlist("recipe_method[]"),
            "recipe_image": request.form.get("recipe_image"),
            "date_created": datetime.today(),
            "created_by": session['user']
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("recipes"))

    return render_template("add_recipe.html")


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """ Search for recipe via ObjectId and update user input in db """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if request.method == "POST":
        update_recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_time": int(request.form.get("recipe_time")),
            "recipe_difficulty": request.form.get("recipe_difficulty"),
            "category": request.form.get("recipe_category"),
            "recipe_ingredients": request.form.getlist("recipe_ingredient[]"),
            "recipe_method": request.form.getlist("recipe_method[]"),
            "recipe_image": request.form.get("recipe_image"),
            "date_created": datetime.today(),
            "created_by": session['user']
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, update_recipe)
        flash("Recipe Successfully Updated")
        return redirect(url_for("recipes"))
    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """ Search for recipe via ObjectId and delete in db """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("recipes"))


@app.route("/show_recipe/<recipe_id>")
def show_recipe(recipe_id):
    """ Search for recipe via ObjectId and return fields from db """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    recipe["date_created"] = recipe["date_created"].strftime("%b %d %Y")
    return render_template(
        "show_recipe.html", recipe=recipe)


@app.route("/blogs")
def blogs():
    """ Retrieve blogs from db and return on Blog page """
    blogs = list(mongo.db.blogs.find().sort("date_created", -1))
    edited_blogs = change_date_format(blogs)
    return render_template("blogs.html", blogs=edited_blogs)


@app.route("/show_blog/<blog_id>")
def show_blog(blog_id):
    """ Search for blog via ObjectId and return fields from db """
    blog = mongo.db.blogs.find_one({"_id": ObjectId(blog_id)})
    blog["date_created"] = blog["date_created"].strftime("%b %d %Y")
    return render_template("show_blog.html", blog=blog)


@app.route("/add_blog", methods=["GET", "POST"])
def add_blog():
    """ Create new blog in db """
    if request.method == "POST":
        blog = {
            "blog_title": request.form.get("blog_title"),
            "blog_description": request.form.get("blog_description"),
            "blog_image": request.form.get("blog_image"),
            "blog_time": int(request.form.get("blog_time")),
            "blog_author": request.form.get("blog_author"),
            "blog_text": request.form.get("blog_text"),
            "date_created": datetime.today()
        }
        mongo.db.blogs.insert_one(blog)
        flash("Blog Successfully Uploaded!")
        return redirect(url_for("blogs"))

    return render_template("add_blog.html")


@app.route("/delete_blog/<blog_id>")
def delete_blog(blog_id):
    """ Search for blog via ObjectId and delete in db """
    mongo.db.blogs.remove({"_id": ObjectId(blog_id)})
    flash("Blog Successfully Deleted")
    return redirect(url_for("blogs"))


@app.route("/edit_blog/<blog_id>", methods=["GET", "POST"])
def edit_blog(blog_id):
    """ Search for blog via ObjectId and update user input in db """
    blog = mongo.db.blogs.find_one({"_id": ObjectId(blog_id)})
    if request.method == "POST":
        update_blog = {
            "blog_title": request.form.get("blog_title"),
            "blog_description": request.form.get("blog_description"),
            "blog_image": request.form.get("blog_image"),
            "blog_time": int(request.form.get("blog_time")),
            "blog_author": request.form.get("blog_author"),
            "blog_text": request.form.get("blog_text"),
            "date_created": datetime.today()
        }
        mongo.db.blogs.update({"_id": ObjectId(blog_id)}, update_blog)
        flash("Blog Successfully Updated")
        return redirect(url_for("blogs"))
    return render_template("edit_blog.html", blog=blog)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=bool(os.environ.get("DEBUG")))

import os, re
from flask import (
    Flask, flash, render_template,
    redirect, session, url_for,
    request)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    recipes = list(mongo.db.recipes.find())
    return render_template("index.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
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
    if request.method == "POST":
        # Check if username exists in db
        exisiting_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if exisiting_user:
            # Ensure password is correct
            if check_password_hash(
            exisiting_user["password"], request.form.get("password")):
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
    username = mongo.db.users.find_one(
        {"username": session['user']})
    recipes = list(mongo.db.recipes.find())
    # Redirect user to profile page
    if session["user"]:
        return render_template(
            "profile.html", username=username, recipes=recipes)
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Log user out of profile
    session.clear()
    flash("Your have successfully logged out")
    return redirect(url_for("login"))


@app.route("/recipes", methods=["GET", "POST"])
def recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_time": request.form.get("recipe_time"),
            "recipe_difficulty": request.form.get("recipe_difficulty"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "recipe_image": request.form.get("recipe_image"),
            "created_by": session['user']
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("recipes"))

    return render_template("add_recipe.html")


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if request.method == "POST":
        update_recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_time": request.form.get("recipe_time"),
            "recipe_difficulty": request.form.get("recipe_difficulty"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "recipe_image": request.form.get("recipe_image"),
            "created_by": session['user']
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, update_recipe)
        flash("Recipe Successfully Updated")
        return redirect(url_for("recipes"))
    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfullt Deleted")
    return redirect(url_for("recipes"))


@app.route("/show_recipe/<recipe_id>")
def show_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    ingredients = recipe["recipe_ingredients"]
    ingredient = re.split(', |and', ingredients)
    return render_template(
        "show_recipe.html", recipe=recipe, ingredient=ingredient)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

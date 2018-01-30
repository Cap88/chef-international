# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify
from flask_jsglue import JSGlue
from chef.helpers import *

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py
jsglue = JSGlue(app)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('CHEF_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route("/", methods=["GET", "POST"])
def index():
    """Render map."""
	# if user reached route via POST (as by submitting a form via POST)
#    if request.method == "POST":

        # request the recipes info via url
#        recipes = lookup()

    # else if user reached route via GET (as by clicking a link or via redirect)
#    else:
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/recipes")
def recipes():
    """Look up recipes for country."""
    country = request.args.get("country")
    results_from = int(request.args.get("pi")) * 10
    results_to = int(results_from) + 10
	
    # ensure parameters are present
    if not request.args.get("country"):
        raise RuntimeError("missing country")

    recipes = lookup(country, results_from, results_to)
    return jsonify(recipes)
import os
### import flask and template for error handling
from flask import Flask,  render_template
### import mysql connector
from flask_mysqldb import MySQL
from .db import set_up_database
from .db.setup import set_up_database


app = Flask(__name__)

### init the connector to connect to the database - global var
#mysql = MySQL(app)
mysql = MySQL()

### create the web app which will run on local server http://127.0.0.1:5000 (default port)
def create_app():
    ### should this debug be set here - it's already in run.py
    ###app.debug=True


    ### scratch - init connector for app
    ### REF: week7.5
    mysql.init_app(app) ### init the mysql connector with the app
    
    ### register the blueprint routes for views - to create the routes for the web app
    from . import views
    app.register_blueprint(views.bp)
    return app

### error handling for HTTP 404 (not found) and HTTP 500 (internal server error) errors
@app.errorhandler(404) 
# inbuilt function which takes error as parameter 
def not_found(e): 
  return render_template("404.html")

@app.errorhandler(500)
def internal_error(e):
  return render_template("500.html")




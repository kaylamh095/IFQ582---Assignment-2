### import flask and template for error handling
from flask import Flask,  render_template
from flask_login import LoginManager

from .db.setup import set_up_database


app = Flask(__name__)

### MySQL and mysql global variable are in .db.setup
set_up_database(app)

### create the web app which will run on local server http://127.0.0.1:5000 (default port)
def create_app():
    app.config['SECRET_KEY'] = '72fab78649216174245adbad90741cb61fe75a1edd30bdec12c975515a95b43c'
    
    ### register the blueprint routes for views - to create the routes for the web app
    from .views import auth, main, library, scratch
    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)
    app.register_blueprint(library.bp)
    app.register_blueprint(scratch.bp)
    
    
    return app

# Login manager for handling user sessions and authentication, will return the user to the login page if they are not logged in and try to access a protected route
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'
login_manager.init_app(app)

### error handling for HTTP 404 (not found) and HTTP 500 (internal server error) errors
@app.errorhandler(404) 
# inbuilt function which takes error as parameter 
def not_found(e): 
  return render_template("404.html")

@app.errorhandler(500)
def internal_error(e):
  return render_template("500.html")




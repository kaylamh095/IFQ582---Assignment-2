### import flask and template for error handling
from flask import Flask, app,  render_template
from flask_login import LoginManager
from project.models.user import User
from .views import register
from .db.setup import set_up_database
from .db.connection import cursor
from flask_bootstrap import Bootstrap5


login_manager = LoginManager()
login_manager.login_view = 'login.login'  # type: ignore[assignment]
login_manager.login_message_category = 'info'

### create the web app which will run on local server http://127.0.0.1:5000 (default port)
def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = '72fab78649216174245adbad90741cb61fe75a1edd30bdec12c975515a95b43c'
  login_manager.init_app(app)
  Bootstrap5(app)

### MySQL and mysql global variable are in .db.setup
  set_up_database(app)

 ### register the blueprint routes for views - to create the routes for the web app
  from .views import main, library, login, register, scratch, admin, kath, item
  app.register_blueprint(main.bp)
  app.register_blueprint(library.bp)
  app.register_blueprint(login.bp)
  app.register_blueprint(register.bp)
  app.register_blueprint(scratch.bp)
  app.register_blueprint(kath.bp)
  app.register_blueprint(item.bp)
  app.register_blueprint(admin.bp, url_prefix='/admin')
    
### error handling for HTTP 404 (not found) and HTTP 500 (internal server error) errors
  @app.errorhandler(404) 
# inbuilt function which takes error as parameter 
  def not_found(e): 
    return render_template("404.html")

  @app.errorhandler(500)
  def internal_error(e):
    return render_template("500.html")

  return app


# Login manager for handling user sessions and authentication, will return the user to the login page if they are not logged in and try to access a protected route
@login_manager.user_loader
def load_user(user_id):
    cur = cursor()
    cur.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    return User(**user) if user else None


from datetime import datetime
import os
from flask_mysqldb import MySQL
from .connection import cursor

### Global mysql variable, initialised in set_up_database
mysql: MySQL

def get_env_contents(app):
   '''Gets contents of an .env file and puts them in app context for MySQL'''
   env_file = None
   if os.path.exists(".env"):
       env_file = ".env"
   elif os.path.exists("env.txt"):
       env_file = "env.txt"
   else:
      raise Exception("Could not locate .env or env.txt file; please put it in project root.")
   
   config = {'MYSQL_HOST', 'MYSQL_USER', 'MYSQL_PASSWORD', 'MYSQL_DB'}

   with open(env_file) as f:
      for line in f:
         key, value = line.strip().split("=", 1)
         if key in config:
            if not value:
               raise Exception("Your " + env_file + " file needs to specify " + key)
            app.config[key] = value
         else:
            raise Exception("Your " + env_file + " file contains an unrecognised item called" + value)
   # Remaining config item
   app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


def set_up_database(app):
   '''Sets up the database connection and ensures it works, raising errors if it doesn't'''
   global mysql
   get_env_contents(app)

   ### Initialise the mysql global variable
   mysql = MySQL(app)

   with app.app_context():
      # Above is only needed here because db is called outside a route handler.
      # Normally Flask supplies it behind the scenes.
      test_connection()


def test_connection():
   try:
      cur = cursor()
      cur.execute('Select 1')
      cur.close()
   except:
      raise Exception("Database connection failed.")

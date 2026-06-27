def connection():
   '''Supplies a database connection with no type errors'''
   from .setup import mysql
   assert mysql.connection is not None
   return mysql.connection


def cursor():
   '''
   Supplies a more compact cursor without the extra connection code, when
   the connection is not needed later.
   '''
   return connection().cursor()

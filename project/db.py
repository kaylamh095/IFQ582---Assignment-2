from datetime import datetime
from . import mysql
from .models.User import User

def connection():
    assert mysql.connection is not None
    return mysql.connection

def cursor():
    return connection().cursor()


def check_for_user(email, password):
    cur = cursor()
    cur.execute("""
        SELECT user_id, first_name, last_name, email, phone
        FROM user
        WHERE email = %s AND password = %s
    """, (email, password))
    row = cur.fetchone()
    cur.close()
    if row:
        return User(row['first_name'], row['last_name'], row['email'], row['phone'], password)
    return None


def add_user(form):
    conn = connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO users (first_name, last_name, email, phone, password)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, 
    (form.first_name.data, form.last_name.data, form.email.data, form.phone.data, form.password.data))
    conn.commit()
    cur.close()

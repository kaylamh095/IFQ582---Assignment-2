from project.db.setup import mysql
from project.models.user import User

def get_user_role():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT u.id, u.first_name, u.last_name, u.email, u.phone, s.is_admin
        FROM user u
        INNER JOIN library_staff s ON u.id = s.user_ID;""")
    user_data = cur.fetchall()
    cur.close()
    return [User(
        first_name=row['first_name'],
        last_name=row['last_name'],
        email=row['email'],
        phone=row['phone'],
        password=None,
        ID=str(row['id']),
        is_admin=row['is_admin'] 
    ) for row in user_data]


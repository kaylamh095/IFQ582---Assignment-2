from project.db.setup import mysql
from project.models.access_request import AccessRequest
from project.models.user import User
from project.models.collection_item import CollectionItem

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


def get_collection_items():
    cur = mysql.connection.cursor()
    cur.execute("SELECT item_id, title, description, image_link, item_category, cultural_group, review_status, access_level, sensitivity_notes FROM collection_items")
    items = cur.fetchall()
    cur.close()
    return [CollectionItem(
        item_id=str(row['item_id']),
        title=row['title'],
        description=row['description'],
        image_link=row['image_link'],
        item_category=row['item_category'],
        cultural_group=row['cultural_group'],
        review_status=row['review_status'],
        access_level=row['access_level'], 
        sensitivity_notes=row['sensitivity_notes']
    ) for row in items]  

def get_item_by_id(item_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT item_id, title, description, image_link, item_category, cultural_group, review_status, access_level, sensitivity_notes FROM collection_items WHERE item_id = %s", (item_id,))
    row = cur.fetchone()
    cur.close()
    return row
    
    
def get_access_requests():
    cur = mysql.connection.cursor()
    cur.execute("SELECT request_id, item_id, member_id, request_status, review_timestamp FROM access_request")
    requests = cur.fetchall()
    cur.close()
    return [AccessRequest(
        request_id=str(row['request_id']),
        item_id=str(row['item_id']),
        member_id=str(row['member_id']),
        request_status=row['request_status'],
        review_timestamp=row['review_timestamp']
    ) for row in requests]

def get_account_info(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT first_name, last_name, email, phone, password FROM user WHERE id = %s", (ID))
    row = cur.fetchone()
    cur.close()
    if row:
        return User(
            first_name=row['first_name'],
            last_name=row['last_name'],
            email=row['email'],
            phone=row['phone'],
            password=None,
            ID=str(row['id']),
        ) 
    return None
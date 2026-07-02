from project.forms import RegisterPublicForm, RegisterCommunityElderForm, RegisterLibraryStaffForm

from .connection import cursor, connection
from ..models.user import User


def email_exists(email):
    cur = cursor()
    cur.execute("SELECT ID FROM user WHERE email = %s", (email,))
    row = cur.fetchone()
    cur.close()
    return row is not None


def check_for_user(email, password):
    '''
    Takes email and hashed password. 
    Returns User and three fields: is_staff, is_admin, is_elder
    '''
    cur = cursor()
    cur.execute("""
        SELECT ID, first_name, last_name, email, phone, ls.employee_ID, ls.is_admin, ce.elder_ID
        FROM user u
        LEFT join library_staff ls on u.ID = ls.user_id
        LEFT join community_elder ce on u.ID = ce.user_id
        WHERE email = %s AND password = %s
    """, (email, password))
    row = cur.fetchone()
    cur.close()
    is_staff = False
    is_admin = False
    is_elder = False
    if row:
         if row['employee_ID']:
            is_staff = True
         if row['is_admin']:
            is_admin = True
         if row['elder_ID']:
            is_elder = True
         return ( User(row['first_name'], row['last_name'], 
                  row['email'], row['phone'], password, ID=row['ID']),
                  is_staff, is_admin, is_elder)
    return None


def add_public_user(form: RegisterPublicForm):
   '''Receives the public user form and creates the user. Returns True on success.'''
   conn = connection()
   cur = conn.cursor()
   p = form.to_public_user()

   try:
      # Create parent user
      cur.execute("""
         INSERT INTO user (first_name, last_name, email, phone, password)
         VALUES (%s, %s, %s, %s, %s)
      """,
      (p.first_name, p.last_name, p.email, p.phone, p.password))

      # Fetch newly created user ID
      user_id = cur.lastrowid
      if not user_id:
         conn.rollback()
         raise Exception("No user ID received back")

      # Create public user
      cur.execute("""
         INSERT INTO public_user (user_id)
         VALUES (%s)
      """, (user_id,))
      conn.commit()
      return True

   except Exception as e:
      conn.rollback()
      print(f"Transaction failed with error: {e}")
      return False
   finally:
      cur.close()


def add_library_staff(form: RegisterLibraryStaffForm):
   '''Receives the library staff user registration form and creates the user. Returns True on success.'''
   conn = connection()
   cur = conn.cursor()
   s = form.to_library_staff()

   try:
      # Create parent user
      cur.execute("""
         INSERT INTO user (first_name, last_name, email, phone, password)
         VALUES (%s, %s, %s, %s, %s)
      """,
      (s.first_name, s.last_name, s.email, s.phone, s.password))

      # Fetch newly created user ID
      user_id = cur.lastrowid
      if not user_id:
         conn.rollback()
         raise Exception("No user ID received back")

      # Create library staff user
      cur.execute("""
         INSERT INTO library_staff (position_title, start_date, is_admin, user_id)
         VALUES (%s, %s, %s, %s)
      """, (s.position_title, s.start_date, s.is_admin, user_id))
      conn.commit()
      return True

   except Exception as e:
      conn.rollback()
      print(f"Transaction failed with error: {e}")
      return False
   finally:
      cur.close()


def add_community_elder(form: RegisterCommunityElderForm):
   '''Receives the community elder registration form and creates the user. Returns True on success.'''
   conn = connection()
   cur = conn.cursor()
   e = form.to_community_elder()

   try:
      # Create parent user
      cur.execute("""
         INSERT INTO user (first_name, last_name, email, phone, password)
         VALUES (%s, %s, %s, %s, %s)
      """,
      (e.first_name, e.last_name, e.email, e.phone, e.password))

      # Fetch newly created user ID
      user_id = cur.lastrowid
      if not user_id:
         conn.rollback()
         raise Exception("No user ID received back")

      # Create community elder
      cur.execute("""
         INSERT INTO community_elder (community_name, user_id)
         VALUES (%s, %s)
      """, (e.community_name, user_id))
      conn.commit()
      return True

   except Exception as e:
      conn.rollback()
      print(f"Transaction failed with error: {e}")
      return False
   finally:
      cur.close()
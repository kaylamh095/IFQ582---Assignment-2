### items.py
### import flask and template for error handling
from flask import Flask,  render_template, Blueprint, request
from ..db.connection import cursor, connection
from ..models.collitem import CollItem

bp = Blueprint('search', __name__)

@bp.route('/search', methods=['GET', 'POST'])
def search():
    pass
#    results = []
#    search_query = request.args.get('query', '')
#
#    try:
#        cur = cursor()
#        sql_query = "SELECT * FROM collection_items WHERE title LIKE %s OR description LIKE %s"
#        search_term = f"%{search_query}%"
#       cur.execute(sql_query, (search_term, search_term))
#        results = cur.fetchall()
#        if request.method == 'POST':
#            search_query = request.form.get('query', '')
#            sql_query = "SELECT * FROM collection_items WHERE title LIKE %s OR description LIKE %s"
#            search_term = f"%{search_query}%"
#            cursor.execute(sql_query, (search_term, search_term))
#            results = cursor.fetchall()
#            cur.close()
#            connection().close()
#    except mysql.connector.Error as err:
#        print(f"Error: {err}")
#    return render_template('search.html', results=results, query=search_query)


### REF:
### Costa, Jose Ortis. (2019). Search Utility with Flask and MySQL. Medium. https://medium.com/@joseortizcosta/search-utility-with-flask-and-mysql-60bb8ee83dad.
### John Elder. (2021). Search Blog Posts From Navbar - Flask Fridays #31. YouTube. https://www.youtube.com/watch?v=kmtZTo-_gJY.
### Ochoa, Brandon. (2023). Building a Search Feature in a Python Flask App. Ochoa Projects. https://ochoaprojects.com/posts/FlaskAppWithSimpleSearch.


### items.py
### import flask and template for error handling
from flask import Flask,  render_template, Blueprint, request
from ..db.connection import cursor, connection
from ..models.collitem import CollItem

bp = Blueprint('search', __name__)

### REF: (John Elder, 2021)
### search page form
@bp.route('/search')
def search():
    #pass
    title = "Search"
    return render_template('search.html', title=title)


### REF: (John Elder, 2021)
### post search results to searchresults.html
### uses POST method only, so you can't access it via URL, only via form submission
@bp.route('/searchresults', methods=['POST'])
def searchresults():
    #pass
    title = "Search Results"

    search_term = request.form.get('search_term')
    filter_category = request.form.get('filter_category')
    filter_access = request.form.get('filter_access')

    return render_template('searchresults.html', title=title, search_term=search_term, filter_category=filter_category, filter_access=filter_access)






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


### REFERENCES:
### Costa, Jose Ortis. (2019). Search Utility with Flask and MySQL. Medium. https://medium.com/@joseortizcosta/search-utility-with-flask-and-mysql-60bb8ee83dad.
### John Elder. (2021). Search Blog Posts From Navbar - Flask Fridays #31. YouTube. https://www.youtube.com/watch?v=kmtZTo-_gJY.
### Ochoa, Brandon. (2023). Building a Search Feature in a Python Flask App. Ochoa Projects. https://ochoaprojects.com/posts/FlaskAppWithSimpleSearch.


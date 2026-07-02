### search.py
### import flask and template for error handling
from flask import Flask,  render_template, Blueprint, request
from ..db.connection import cursor
from ..models.collitem import CollItem

bp = Blueprint('search', __name__)

### REF: (John Elder, 2021)
### search page form
### send results to search page under the search form area - needs GET & POST methods to do this
@bp.route('/search', methods=['GET', 'POST'])
def search():
    #pass
    title = "Search"
    results = []
    query = ''
    filter_by_category = ''
    filter_by_access = ''



    if request.method == 'POST':

        query = request.form.get('search_query') ### from search form input field
        filter_by_category = request.form.get('filter_category')
        filter_by_access = request.form.get('filter_access')

        search_term = ('%' + query + '%')
        print(f"Received search query: {query}")  # print the received search query to the console
        print(f"Received filter category: {filter_by_category}")  # print the received filter category to the console
        print(f"Received filter access: {filter_by_access}")  # print the received filter access to the console


        #sql_query = "SELECT * FROM collection_items WHERE title LIKE %s OR description LIKE %s"
        #search_term = ('%' + query + '%')


        try:
            cur = cursor()
            #cur = cursor(dictionary=True)
            #cur = cursorDict() ### 

            if filter_by_category == "" and filter_by_access == "":
                ### search without filters
                cur.execute("SELECT * FROM collection_items WHERE (title LIKE %s OR description LIKE %s) ORDER BY title", (search_term, search_term))
            elif filter_by_category != "" and filter_by_access == "":
                ### search with category filter only
                cur.execute("SELECT * FROM collection_items WHERE (title LIKE %s OR description LIKE %s) AND item_category = %s", (search_term, search_term, filter_by_category))
            elif filter_by_category == "" and filter_by_access != "":
                ### search with access filter only
                cur.execute("SELECT * FROM collection_items WHERE (title LIKE %s OR description LIKE %s) AND access_level = %s", (search_term, search_term, filter_by_access))
            else:
                ### search with both filters
                cur.execute("SELECT * FROM collection_items WHERE (title LIKE %s OR description LIKE %s) AND item_category = %s AND access_level = %s", (search_term, search_term, filter_by_category, filter_by_access))
            

            
            #cur.execute("SELECT title, description FROM collection_items WHERE title LIKE %s OR description LIKE %s ORDER BY title", (search_term, search_term))
            ## OK: cur.execute("SELECT * FROM collection_items WHERE title LIKE %s OR description LIKE %s ORDER BY title", (search_term, search_term))
            
            #print(f"SELECT title, description FROM collection_items WHERE title LIKE %s OR description LIKE %s", (search_term, search_term))  # Debugging line to print the executed SQL query

            #cur.execute(sql_query)  ### execute the query
            results = cur.fetchall()
            print(f"SQL query results: {results}")  # Debugging line to print the executed SQL query results
            cur.close()
            #connection().close() ### don't close the connection here - it's before results returned to the template, which needs the connection open to display results (closes elsewhere in the app)
            #itemsall = [CollItem(item_id=str(row['item_id']), title=row['title'], description=row['description'], image_link=row['image_link'], item_category=row['item_category'], cultural_group=row['cultural_group'], sensitivity_notes=row['sensitivity_notes'], review_status=row['review_status'], access_level=row['access_level']) for row in results]  ### create a list of CollItem objects with the results
        except Exception as e:
            print(f"Error: {e}")


    return render_template('search.html', title=title, results=results, query=query, search_query=query, filter_category=filter_by_category, filter_access=filter_by_access)  ### pass the data to the search template to display # results= needs to match the jinja2 in search statement in search.html
### search_query=query, filter_category=filter_by_category, filter_access=filter_by _access, search_query=query,



    #cur = cursor() ### open a cursor to the db
    #cur.execute("SELECT item_id, title, description, image_link, item_category, cultural_group, sensitivity_notes, review_status, access_level FROM collection_items") ### run the query
    #results = cur.fetchall() ### get all query results
    #cur.close() ### close the cursor
    #itemsall = [CollItem(item_id=str(row['item_id']), title=row['title'], description=row['description'], image_link=row['image_link'], item_category=row['item_category'], cultural_group=row['cultural_group'], sensitivity_notes=row['sensitivity_notes'], review_status=row['review_status'], access_level=row['access_level']) for row in results]  ### create a list of CollItem objects with the results
  


### REF: (John Elder, 2021)
### post search results to searchresults.html
### uses POST method only, so you can't access it via URL, only via form submission
#@bp.route('/searchresults', methods=['POST'])
#def searchresults():
#    #pass
#    title = "Search Results"
#
#    search_term = request.form.get('search_term')
#    filter_category = request.form.get('filter_category')
#    filter_access = request.form.get('filter_access')
#
#    return render_template('searchresults.html', title=title, search_term=search_term, filter_category=filter_category, filter_access=filter_access)






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
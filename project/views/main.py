### REF: IFQ582-5.8
### import flask and blueprint / route template
from flask import Blueprint, render_template, request
from project.db.admin_db import get_featured_items
from ..db.items_db import get_all_items_from_db, get_one_item_from_db
from ..db.search_db import search_db



bp = Blueprint('main', __name__) 

@bp.route('/', methods=['GET', 'POST'])
def index():
    featured_items = get_featured_items()


    ### search on homepage - send results to home page under the search form area - needs GET & POST methods to do this
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

        try:
            results = search_db(search_term, filter_by_category, filter_by_access)  ### call the search_db function to perform the search and get results

        except Exception as e:
            print(f"Error: {e}")

    #return render_template('index.html', results=results, query=query, search_query=query, filter_category=filter_by_category, filter_access=filter_by_access)  ### pass the data to the search template to display # results= needs to match the jinja2 in search statement in search.html

    return render_template('index.html', title='Featured Collection Items', featured_items=get_featured_items(), results=results, query=query, search_query=query, filter_category=filter_by_category, filter_access=filter_by_access)


### REF: (John Elder, 2021)
### search page form
### send results to search page under the search form area - needs GET & POST methods to do this
#@bp.route('/', methods=['GET', 'POST'])
#def search_via_homepage():
    #title = "Search"
#    results = []
#    query = ''
#    filter_by_category = ''
#    filter_by_access = ''
#
#    if request.method == 'POST':
#
#        query = request.form.get('search_query') ### from search form input field
#        filter_by_category = request.form.get('filter_category')
#        filter_by_access = request.form.get('filter_access')
#
#        search_term = ('%' + query + '%')
#        print(f"Received search query: {query}")  # print the received search query to the console
#        print(f"Received filter category: {filter_by_category}")  # print the received filter category to the console
#        print(f"Received filter access: {filter_by_access}")  # print the received filter access to the console
#
#        try:
#            results = search_db(search_term, filter_by_category, filter_by_access)  ### call the search_db function to perform the search and get results
#
#        except Exception as e:
#            print(f"Error: {e}")
#
#    return render_template('index.html', results=results, query=query, search_query=query, filter_category=filter_by_category, filter_access=filter_by_access)  ### pass the data to the search template to display # results= needs to match the jinja2 in search statement in search.html

### kath.py
### import flask and template for error handling
from flask import Flask,  render_template, Blueprint, request
from ..db.connection import cursor, connection


bp = Blueprint('kath', __name__)

### scratch testing page
### @app.route('/scratch')
@bp.route('/kath')
def kath():
    cur = cursor() ### open a cursor to the db
       
    cur.execute("SELECT item_id, title, description, image_link, item_category, item_category, cultural_group, sensitivity_notes, review_status, access_level FROM collection_items WHERE item_id = 1") ### run the query
    results = cur.fetchall() ### get all query results
    cur.close() ### close the cursor
    return render_template('kath.html', items=results) ### pass the data to the scratch template to display
   
    
    #cur.execute("SELECT * FROM collection_items where item_id = 1") ### run the query
    #cur.execute("SELECT item_id, title, description, image_link, item_category AS item_type, item_category, cultural_group AS access_considerations, sensitivity_notes AS sensitivity_level, review_status, access_level AS access_status FROM collection_items WHERE item_id = 1") ### run the query
    #cur.execute("SELECT item_id, title, description, image_link, item_category, cultural_group, sensitivity_notes, review_status, access_level FROM collection_items") ### run the query
    #cur.execute("SELECT title FROM collection_items") ### run the query
    
    
    
    #results = cur.fetchone() ### get one query result
    #row = cur.fetchone() ### get one query result
    
    
    #item = CollectionItem(int(results['item_id']), results['title'], results['description'], results['image_link'], results['item_type'], results['item_category'], results['review_status'], results['access_status'], results['access_considerations'], results['sensitivity_level'])  ### create a CollectionItem object with the results
    
    ### items = results  ### create an Item object with the results
    
    ###return render_template('scratch.html', items=items) ### pass the data to the scratch template to display
    #return render_template('scratch.html', items=results) ### pass the data to the scratch template to display
    #return render_template('scratch.html', data=results) ### pass the data to the template to display
    
    ###return str(results) ### return the results as a string to the browser for initial testing -- worked OK

    #return [CollectionItem(int(row['item_id']), row['title'], row['description'], row['image_link'], row['item_type'], row['item_category'], row['review_status'], row['access_status'], row['access_considerations'], row['sensitivity_level']) for row in results]  ### return a CollectionItem object
    
    #return item  ### return a CollectionItem object




#def get_items():
#    cur = cursor() ### open a cursor to the db
#    #cur.execute("SELECT * FROM collection_items where item_id = 1") ### run the query
#    cur.execute("SELECT item_id, title, description, image_link, item_category, cultural_group, sensitivity_notes, review_status, access_level FROM collection_items WHERE item_id = 1") ### run the query
#    #cur.execute("SELECT item_id, title, description, image_link, item_category, cultural_group, sensitivity_notes, review_status, access_level FROM collection_items") ### run the query
#    #cur.execute("SELECT title FROM collection_items") ### run the query
#    results = cur.fetchall() ### get all query results
#    cur.close() ### close the cursor
#    #return render_template('scratch.html', data=results) ### pass the data to the template to display
#    #return str(results) ### return the results as a string to the browser for initial testing -- worked OK
#    #return render_template('itemsall.html', data=results)
#    items = Item(results)  ### create an Item object with the results
##    return 
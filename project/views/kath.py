### kath.py
### import flask and template for error handling
from flask import Flask,  render_template, Blueprint, request
from ..db.connection import cursor, connection
from ..models.collection_item import CollectionItem
from ..models.item import Item

bp = Blueprint('kath', __name__)

### kath testing page
@bp.route('/kath')
def kath():
    cur = cursor() ### open a cursor to the db
#       
    cur.execute("SELECT item_id, title, description, image_link, item_category, cultural_group, sensitivity_notes, review_status, access_level FROM collection_items") ### run the query
    #cur.execute("SELECT item_id, title, description, image_link, item_category AS item_type, item_category, cultural_group AS access_considerations, sensitivity_notes AS sensitivity_level, review_status, access_level AS access_status FROM collection_items") ### run the query
    ##cur.execute("SELECT item_id, title, description, image_link, item_category AS item_type, item_category, cultural_group, sensitivity_notes AS sensitivity_level, review_status, access_level FROM collection_items") ### run the query
    
    results = cur.fetchall() ### get all query results
    cur.close() ### close the cursor
#    return render_template('kath.html', items=results) ### pass the data to the scratch template to display
    items = [Item(item_id=str(row['item_id']), title=row['title'], description=row['description'], image_link=row['image_link'], item_category=row['item_category'], cultural_group=row['cultural_group'], sensitivity_notes=row['sensitivity_notes'], review_status=row['review_status'], access_level=row['access_level']) for row in results]  ### create a list of Item objects with the results
    return render_template('kath.html', items=items) ### pass the data to the kath template to display # items= needs to match the jinja x in items statement in kath.html
    #return [Item(item_id=str(row['item_id']), title=row['title'], description=row['description'], image_link=row['image_link'], item_category=row['item_category'], cultural_group=row['cultural_group'], sensitivity_notes=row['sensitivity_notes'], review_status=row['review_status'], access_level=row['access_level']) for row in items]  ### return an Item object
    #return [CollectionItem(item_id=str(row['item_id']), title=row['title'], description=row['description'], image_link=row['image_link'], item_type=row['item_type'], item_category=row['item_category'], review_status=row['review_status'], access_considerations=row['access_considerations'], access_status=row['access_status'], sensitivity_level=row['sensitivity_level']) for row in items]  ### return a CollectionItem object
    
    
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


### from miltontours
#def get_cities():
#    cur = mysql.connection.cursor()
#    cur.execute("SELECT city_id, city_name, city_description, city_image FROM cities")
#    results = cur.fetchall()
#    cur.close()
#    return [City(str(row['city_id']), row['city_name'], row['city_description'], row['city_image']) for row in results]


####################################

#def get_item(item_id):
#    cur = cursor() ### open a cursor to the db
#    cur.execute("SELECT item_id, title, description, image_link, item_category, item_category, cultural_group, sensitivity_notes, review_status, access_level FROM collection_items WHERE item_id = 1") ### run the query
#    #cur.execute("SELECT item_id, title, description, image_link, item_category, cultural_group, sensitivity_notes, review_status, access_level FROM collection_items WHERE item_id = %s", (item_id,)) ### run the query
#    #results = cur.fetchone() ### get one query result
#    row = cur.fetchall() ### get one query result
#    cur.close() ### close the cursor
#    #item = Item(results['item_id'], results['title'], results['description'], results['image_link'], results['item_category'], results['cultural_group'], results['sensitivity_notes'], results['review_status'], results['access_level'])  ### create an Item object with the results
#    #return item  ### return the results as a dictionary
#   #print(results)  ### print the results to the console for testing
#    return [Item(str(row['item_id']), row['title'], row['description'], row['image_link'], row['item_category'], row['cultural_group'], row['sensitivity_notes'], row['review_status'], row['access_level']) for row in rows]  ### create a list of Item objects with the results


#@bp.route('/kath')
#def kath(item_id):
#    item = get_item(item_id)
#    return render_template('kath.html', item=item)


## scratch testing page
### @app.route('/scratch')
#@bp.route('/kath')
#def kath():
#    cur = cursor() ### open a cursor to the db
#       
#    cur.execute("SELECT item_id, title, description, image_link, item_category, item_category, cultural_group, sensitivity_notes, review_status, access_level FROM collection_items WHERE item_id = 1") ### run the query
#    results = cur.fetchall() ### get all query results
#    cur.close() ### close the cursor
#    return render_template('scratch.html', items=results) ### pass the data to the scratch template to display
  
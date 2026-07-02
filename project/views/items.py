### items.py
### import flask and template for error handling
from flask import Flask,  render_template, Blueprint, request
from ..db.connection import cursor, connection
from ..models.collitem import CollItem

bp = Blueprint('items', __name__)

### /item route to display all items in the collection_items table in the CollItem class
@bp.route('/items')
def items():
    cur = cursor() ### open a cursor to the db
    cur.execute("SELECT item_id, title, description, image_link, item_category, cultural_group, sensitivity_notes, review_status, access_level FROM collection_items") ### run the query
    results = cur.fetchall() ### get all query results
    cur.close() ### close the cursor
    itemsall = [CollItem(item_id=str(row['item_id']), title=row['title'], description=row['description'], image_link=row['image_link'], item_category=row['item_category'], cultural_group=row['cultural_group'], sensitivity_notes=row['sensitivity_notes'], review_status=row['review_status'], access_level=row['access_level']) for row in results]  ### create a list of CollItem objects with the results
    return render_template('items.html', items=itemsall) ### pass the data to the item template to display # items= needs to match the jinja2 in items statement in items.html



#### /item route to display all items in the collection_items table in the CollItem class
#@bp.route('/item/<int:item_id>')
#def item():
#    cur = cursor() ### open a cursor to the db
#    cur.execute("SELECT item_id, title, description, image_link, item_category, cultural_group, sensitivity_notes, review_status, access_level FROM collection_items WHERE item_id = %s", (request.view_args['item_id'],)) ### run the query
#    results = cur.fetchone() ### get the query resultq
#    cur.close() ### close the cursor
#   item = CollItem(item_id=str(results['item_id']), title=results['title'], description=results['description'], image_link=results['image_link'], item_category=results['item_category'], cultural_group=results['cultural_group'], sensitivity_notes=results['sensitivity_notes'], review_status=results['review_status'], access_level=results['access_level'])  ### create a CollItem object from the results
#    return render_template('item.html', item=item) ### pass the data to the item template to display # item= needs to match the jinja x in item statement in item.html
  
    
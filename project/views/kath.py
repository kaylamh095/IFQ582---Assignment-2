### kath.py
### import flask and template for error handling
from flask import Flask,  render_template, Blueprint, request
from ..db.connection import cursor, connection
from ..models.collitem import CollItem

bp = Blueprint('kath', __name__)

### /kath route to display all items in the collection_items table in the Item class
@bp.route('/kath')
def kath():
    cur = cursor() ### open a cursor to the db
    cur.execute("SELECT item_id, title, description, image_link, item_category, cultural_group, sensitivity_notes, review_status, access_level FROM collection_items") ### run the query
    results = cur.fetchall() ### get all query results
    cur.close() ### close the cursor
    items = [CollItem(item_id=str(row['item_id']), title=row['title'], description=row['description'], image_link=row['image_link'], item_category=row['item_category'], cultural_group=row['cultural_group'], sensitivity_notes=row['sensitivity_notes'], review_status=row['review_status'], access_level=row['access_level']) for row in results]  ### create a list of Item objects with the results
    return render_template('kath.html', items=items) ### pass the data to the item template to display # items= needs to match the jinja x in items statement in item.html
    
    
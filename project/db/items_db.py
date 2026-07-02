### items.py
### import flask and template for error handling
from flask import Flask,  render_template, Blueprint, request
from ..db.connection import cursor, connection
from ..models.collitem import CollItem

def get_all_items_from_db():
    cur = cursor() ### open a cursor to the db
    cur.execute("SELECT item_id, title, description, image_link, item_category, cultural_group, sensitivity_notes, review_status, access_level FROM collection_items") ### run the query
    results = cur.fetchall() ### get all query results
    cur.close() ### close the cursor
    itemsall = [CollItem(item_id=(row['item_id']), title=row['title'], description=row['description'], image_link=row['image_link'], item_category=row['item_category'], cultural_group=row['cultural_group'], sensitivity_notes=row['sensitivity_notes'], review_status=row['review_status'], access_level=row['access_level']) for row in results]  ### create a list of CollItem objects with the results
    #return render_template('items.html', items=itemsall) ### pass the data to the item template to display # items= needs to match the jinja2 in items statement in items.html
    return itemsall ### return the list of CollItem objects - all items


def get_one_item_from_db(item_id):
    cur = cursor() ### open a cursor to the db
    cur.execute("SELECT item_id, title, description, image_link, item_category, cultural_group, sensitivity_notes, review_status, access_level FROM collection_items WHERE item_id = %s", (item_id,)) ### run the query
    row = cur.fetchone() ### get the query results
    cur.close() ### close the cursor
    return CollItem(item_id=row['item_id'], title=row['title'], description=row['description'], image_link=row['image_link'], item_category=row['item_category'], cultural_group=row['cultural_group'], sensitivity_notes=row['sensitivity_notes'], review_status=row['review_status'], access_level=row['access_level']) if row else None  ### create a single CollItem object with the results
    #return render_template('items.html', items=itemsall) ### pass the data to the item template to display # items= needs to match the jinja2 in items statement in items.html
    #return one_item ### return the list of CollItem objects - the single item

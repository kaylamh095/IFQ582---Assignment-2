### search_db.py
### import flask and template for error handling
from flask import Flask,  render_template, Blueprint, request
from ..db.connection import cursor
from ..models.collitem import CollItem



def search_db(search_term, filter_by_category, filter_by_access):
    
            cur = cursor()

            if filter_by_category == "" and filter_by_access == "":
                ### search without filters
                cur.execute("SELECT item_id, title, description, image_link, item_category, cultural_group, sensitivity_notes, review_status, access_level FROM collection_items WHERE (title LIKE %s OR description LIKE %s) ORDER BY title", (search_term, search_term))
            elif filter_by_category != "" and filter_by_access == "":
                ### search with category filter only
                cur.execute("SELECT item_id, title, description, image_link, item_category, cultural_group, sensitivity_notes, review_status, access_level FROM collection_items WHERE (title LIKE %s OR description LIKE %s) AND item_category = %s", (search_term, search_term, filter_by_category))
            elif filter_by_category == "" and filter_by_access != "":
                ### search with access filter only
                cur.execute("SELECT item_id, title, description, image_link, item_category, cultural_group, sensitivity_notes, review_status, access_level FROM collection_items WHERE (title LIKE %s OR description LIKE %s) AND access_level = %s", (search_term, search_term, filter_by_access))
            else:
                ### search with both filters
                cur.execute("SELECT item_id, title, description, image_link, item_category, cultural_group, sensitivity_notes, review_status, access_level FROM collection_items WHERE (title LIKE %s OR description LIKE %s) AND item_category = %s AND access_level = %s", (search_term, search_term, filter_by_category, filter_by_access))
            

            
            #cur.execute("SELECT title, description FROM collection_items WHERE title LIKE %s OR description LIKE %s ORDER BY title", (search_term, search_term))
            ## OK: cur.execute("SELECT * FROM collection_items WHERE title LIKE %s OR description LIKE %s ORDER BY title", (search_term, search_term))
            
            #print(f"SELECT title, description FROM collection_items WHERE title LIKE %s OR description LIKE %s", (search_term, search_term))  # Debugging line to print the executed SQL query

            #cur.execute(sql_query)  ### execute the query
            results = cur.fetchall()
            print(f"SQL query results: {results}")  # Debugging line to print the executed SQL query results
            cur.close()
            #connection().close() ### don't close the connection here - it's before results returned to the template, which needs the connection open to display results (closes elsewhere in the app)
            return[CollItem(item_id=str(row['item_id']), title=row['title'], description=row['description'], image_link=row['image_link'], item_category=row['item_category'], cultural_group=row['cultural_group'], sensitivity_notes=row['sensitivity_notes'], review_status=row['review_status'], access_level=row['access_level']) for row in results]  ### create a list of CollItem objects with the results
        
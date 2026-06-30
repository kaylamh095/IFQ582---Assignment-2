### import flask and blueprint / route template
from flask import Blueprint, render_template, flash, url_for, redirect, app
from project.forms import UpdateItemForm
from ..db.setup import mysql
from ..wrappers import only_admins

bp = Blueprint('admin', __name__)

#Route for the admin page
@bp.route('/admin', methods=['GET', 'POST'])
@only_admins
def admin():
    form = UpdateItemForm()
    if form.validate_on_submit():
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO collection_items (title, description, image_link, item_category, cultural_group, sensitivity_notes, review_status, access_level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (form.title.data, form.description.data, form.image_link.data.filename if form.image_link.data else None, form.item_category.data, form.cultural_group.data, form.sensitivity_notes.data, form.review_status.data, form.access_level.data))
        mysql.connection.commit()
        cur.close()
        flash('Item added successfully!', 'success')
        return redirect(url_for('admin.admin'))
    return render_template('admin.html', title='Admin', form=form)



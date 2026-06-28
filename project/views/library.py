### REF: IFQ582-5.8
### import flask and blueprint / route template
from flask import Blueprint, render_template, request, flash, url_for, redirect
# from flask_login import login_required
from project.forms import UpdateItemForm
from ..db.setup import mysql
from ..wrappers import only_admins
from ..db.connection import connection


bp = Blueprint('library', __name__)

@bp.route('/item/', methods = ['POST', 'GET']) 
def item(): 
    if request.method == "POST":

        print('FullName: {}\nEmail: {}\nReason for Access Request: {}'\
            .format(request.values.get('fullName'), request.values.get('email'), request.values.get('reason')))
    
    return render_template('item.html')


@bp.route('/assessment/', methods = ['GET', 'POST']) 
def assessment(): 
    if request.method == "POST":

        print('Review Notes: {}\nReview Outcome: {}\nSensitivity Level: {}\nConditions of Use: {}\nReviewer Name: {}'\
            .format(request.values.get('reviewNotes'), request.values.get('reviewOutcome'), request.values.get('sensitivityLevel'), request.values.get('conditionsofUse'), request.values.get('reviewerName')))

    return render_template('assessment.html')


@bp.route("/admin", methods = ['GET', 'POST'])
# @login_required
@only_admins
def admin():
    form = UpdateItemForm()
    if form.validate_on_submit():
       cur = connection().cursor()
       cur.execute("INSERT INTO collection_items (title, description, image_link, item_category, cultural_group, sensitivity_notes, review_status, access_level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (form.title.data, form.description.data, form.image_link.data.filename if form.image_link.data else None, form.item_category.data, form.cultural_group.data, form.sensitivity_notes.data, form.review_status.data, form.access_level.data))
       connection().commit()
       cur.close()
       flash('Item added successfully!', 'success')
       return redirect(url_for('admin'))
    return render_template('admin.html', title='Admin', form=form) 
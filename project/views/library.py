### REF: IFQ582-5.8
### import flask and blueprint / route template
from flask import Blueprint, render_template, request, flash, url_for, redirect
# from flask_login import login_required
from project.forms import UpdateItemForm
from ..db.setup import mysql
from ..wrappers import only_elders
from ..db.connection import connection


bp = Blueprint('library', __name__)

@bp.route('/item/', methods = ['POST', 'GET']) 
def item(): 
    if request.method == "POST":

        print('FullName: {}\nEmail: {}\nReason for Access Request: {}'\
            .format(request.values.get('fullName'), request.values.get('email'), request.values.get('reason')))
    
    return render_template('item.html')


@bp.route('/assessment/', methods = ['GET', 'POST']) 
@only_elders
def assessment(): 
    if request.method == "POST":

        print('Review Notes: {}\nReview Outcome: {}\nSensitivity Level: {}\nConditions of Use: {}\nReviewer Name: {}'\
            .format(request.values.get('reviewNotes'), request.values.get('reviewOutcome'), request.values.get('sensitivityLevel'), request.values.get('conditionsofUse'), request.values.get('reviewerName')))

    return render_template('assessment.html')



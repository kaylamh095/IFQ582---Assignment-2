### REF: IFQ582-5.8
### import flask and blueprint / route template
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .forms import RegisterForm
#from .db import check_for_user, add_user
from .db.user import check_for_user, add_user
from . import mysql


bp = Blueprint('bp', __name__) 


@bp.route('/', methods = ['GET', 'POST']) 
def index(): 
    return render_template('index.html')


@bp.route('/register/', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Check if the user already exists
            user = check_for_user(form.email.data, form.password.data)
            if user:
                flash('User already exists', 'error')
                return redirect(url_for('main.register'))

            add_user(form)
            flash('Registration successful!')
            return redirect(url_for('main.login'))

    return render_template('register.html', form=form)


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



### scratch testing page
### @app.route('/scratch')
@bp.route('/scratch')
def scratch():
    cur = mysql.connection.cursor() ### open a cursor to the db
    ###cur.execute("SELECT * FROM collection_items") ### run the query
    cur.execute("SELECT title FROM collection_items") ### run the query
    results = cur.fetchall() ### get all query results
    cur.close() ### close the cursor
    ###return render_template('scratch.html', scratch=results) ### pass the data to the template to display
    return str(results) ### return the results as a string to the browser for initial testing -- worked OK


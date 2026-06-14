from flask import Blueprint, render_template, request
bp = Blueprint('bp', __name__) 

 
@bp.route('/index/', methods = ['GET', 'POST']) 

def index(): 

    return render_template('index.html')


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
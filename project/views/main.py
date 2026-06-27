### REF: IFQ582-5.8
### import flask and blueprint / route template
from flask import Blueprint, render_template


bp = Blueprint('main', __name__) 


@bp.route('/', methods = ['GET', 'POST']) 
def index(): 
    return render_template('index.html')

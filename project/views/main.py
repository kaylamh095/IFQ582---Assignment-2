### REF: IFQ582-5.8
### import flask and blueprint / route template
from flask import Blueprint, render_template
from project.db.admin_db import get_featured_items


bp = Blueprint('main', __name__) 

@bp.route('/', methods=['GET', 'POST'])
def index():
    featured_items = get_featured_items()
    return render_template('index.html', title='Featured Collection Items', featured_items=get_featured_items())
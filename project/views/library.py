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



@bp.route('/assessment_dashboard', methods=['GET'])
@only_elders
def assessment_dashboard():
    items = get_all_items()

    return render_template(
        'assessment_dashboard.html',
        items=items
    )


@bp.route('/assessment/<int:item_id>', methods=['GET'])
@only_elders
def assessment(item_id):
    item = get_item(item_id)

    if item is None:
        return "Item not found", 404

    reviews = get_reviews(item_id)
    elders = get_elders()
    latest = reviews[0] if reviews else None

    return render_template(
        'assessment.html',
        item=item,
        reviews=reviews,
        elders=elders,
        latest=latest,
        outcome_labels=OUTCOME_LABELS,
    )


@bp.route('/assessment/<int:item_id>/review', methods=['POST'])
@only_elders
def submit_review(item_id):
    item = get_item(item_id)

    if item is None:
        return "Item not found", 404

    review_notes = request.form.get("reviewNotes", "").strip()
    review_outcome = request.form.get("reviewOutcome", "").strip()
    sensitivity_level = request.form.get("sensitivityLevel", "").strip()
    conditions_of_use = request.form.get("conditionsofUse", "").strip()
    elder_id = request.form.get("elder_id", "").strip()

    valid = (
        review_notes
        and len(review_notes) >= 10
        and review_outcome in OUTCOME_LABELS
        and sensitivity_level in ("Low", "Medium", "High")
        and conditions_of_use
        and elder_id.isdigit()
    )

    if not valid:
        reviews = get_reviews(item_id)
        elders = get_elders()

        return render_template(
            'assessment.html',
            item=item,
            reviews=reviews,
            elders=elders,
            latest=reviews[0] if reviews else None,
            outcome_labels=OUTCOME_LABELS,
            error=(
                "Please complete all required fields. "
                "Review notes need at least 10 characters, and a reviewer must be selected."
            ),
        ), 400

    save_review(
        item_id=item_id,
        elder_id=elder_id,
        review_notes=review_notes,
        review_outcome=review_outcome,
        sensitivity_level=sensitivity_level,
        conditions_of_use=conditions_of_use,
    )

    return redirect(url_for('library.assessment', item_id=item_id))




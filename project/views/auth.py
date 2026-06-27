### REF: IFQ582-5.8
### import flask and blueprint / route template
from flask import Blueprint, render_template, request, flash, redirect, url_for
from hashlib import sha256
from ..forms import RegisterForm
from ..db.user import check_for_user, add_user

bp = Blueprint('auth', __name__)


@bp.route('/register/', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Hash the password
            assert form.password.data
            form.password.data = sha256(form.password.data.encode()).hexdigest()
            # Check if the user already exists
            user = check_for_user(form.email.data, form.password.data)
            if user:
                flash('User already exists', 'error')
                return redirect(url_for('main.register'))
            # User does not exist; create them
            add_user(form)
            flash('Registration successful!')
            return redirect(url_for('main.login'))

    return render_template('register.html', form=form)

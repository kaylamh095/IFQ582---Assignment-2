### REF: IFQ582-5.8
### import blueprint / route template
from flask import Blueprint, render_template, request, flash, redirect, url_for
from hashlib import sha256
from ..forms import RegisterPublicForm, RegisterLibraryStaffForm, RegisterCommunityElderForm
from ..db.user import email_exists, add_public_user, add_library_staff, add_community_elder
from ..wrappers import only_admins

bp = Blueprint('register', __name__)


@bp.route('/register_public/', methods=['POST', 'GET'])
def registerPublicUser():
    form = RegisterPublicForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Hash the password
            assert form.password.data
            form.password.data = sha256(form.password.data.encode()).hexdigest()
            # Check if the user already exists
            if email_exists(form.email.data):
                flash('User already exists', 'error')
                return redirect(url_for('register.registerPublicUser'))
            # User does not exist; create them
            if add_public_user(form):
                flash('Registration successful!')
                return redirect(url_for('login.login'))
            # If got to here, registration didn't work
            flash('Registration failed. Feel free to try again.', 'error')

    return render_template('register.html', form=form)


@bp.route('/register_library_staff/', methods=['POST', 'GET'])
@only_admins
def registerLibraryStaff():
    form = RegisterLibraryStaffForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Hash the password
            assert form.password.data
            form.password.data = sha256(form.password.data.encode()).hexdigest()
            # Check if the user already exists
            if email_exists(form.email.data):
                flash('User already exists', 'error')
                return redirect(url_for('register.registerLibraryStaff'))
            # User does not exist; create them
            if add_library_staff(form):
                flash('Registration successful!')
                return redirect(url_for('login.login'))
            # If got to here, registration didn't work
            flash('Registration failed. Feel free to try again.', 'error')

    return render_template('register.html', form=form)


@bp.route('/register_community_elder/', methods=['POST', 'GET'])
@only_admins
def registerCommunityElder():
    form = RegisterCommunityElderForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Hash the password
            assert form.password.data
            form.password.data = sha256(form.password.data.encode()).hexdigest()
            # Check if the user already exists
            if email_exists(form.email.data):
                flash('User already exists', 'error')
                return redirect(url_for('register.registerCommunityElder'))
            # User does not exist; create them
            if add_community_elder(form):
                flash('Registration successful!')
                return redirect(url_for('login.login'))
            # If got to here, registration didn't work
            flash('Registration failed. Feel free to try again.', 'error')

    return render_template('register.html', form=form)

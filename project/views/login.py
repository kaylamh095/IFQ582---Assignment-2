### REF: IFQ582-5.8
### import blueprint / route template
from flask import Blueprint, render_template, request, flash, redirect, session, url_for
from hashlib import sha256
from flask_login import login_user, current_user
from project.forms import LoginForm
from project.db.user import check_for_user, add_public_user, add_library_staff
from project.models.user import User

bp = Blueprint("login", __name__)


@bp.route("/login/", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            assert form.password.data  # to silence linter warning
            form.password.data = sha256(form.password.data.encode()).hexdigest()
            result = check_for_user(form.email.data, form.password.data)
            if not result:
                flash("Invalid username or password", "error")
                return redirect(url_for("login.login"))

            user, is_staff, is_admin, is_elder = result
            session["user"] = {
                "firstname": user.first_name,
                "surname": user.last_name,
                "email": user.email,
                "phone": user.phone,
                "is_staff": is_staff,
                "is_admin": is_admin,
                "is_elder": is_elder,
            }
            session["logged_in"] = True
            flash("Login successful!")
            return redirect(url_for("main.index"))

    return render_template("login.html", form=form)

@bp.route("/logout/", methods=["GET"])
def logout():
    session.clear()
    return redirect(url_for("login.login"))


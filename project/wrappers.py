from flask import session, redirect, flash, url_for
from functools import wraps

"""
This module provides decorators to limit access to routes.

Example usage:

@bp.route('/manage/')
@only_admins
def manage():
    # code for managing the app

"""

def login_required(func):
    """Decorator to ensure only looged-in users can access the route."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user' not in session:
            flash('Please log in before moving on.', 'error')
            return redirect(url_for('login.login'))
    return wrapper


def only_staff(func):
    """Decorator to ensure that the user is a library staff member."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user' not in session:
            flash('Please log in before moving on.', 'error')
            return redirect(url_for('login.login'))
        if not session['user']['is_staff']:
            flash('You do not have permission to view this page.', 'error')
            return redirect(url_for('main.index'))
        return func(*args, **kwargs)
    return wrapper


def only_admins(func):
    """Decorator to ensure that the user is an admin."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user' not in session:
            flash('Please log in before moving on.', 'error')
            return redirect(url_for('login.login'))
        if not session['user']['is_admin']:
            flash('You do not have permission to view this page.', 'error')
            return redirect(url_for('main.index'))
        return func(*args, **kwargs)
    return wrapper


def only_elders(func):
    """Decorator to ensure that the user is a community elder."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user' not in session:
            flash('Please log in before moving on.', 'error')
            return redirect(url_for('login.login'))
        if not session['user']['is_elder']:
            flash('You do not have permission to view this page.', 'error')
            return redirect(url_for('main.index'))
        return func(*args, **kwargs)
    return wrapper

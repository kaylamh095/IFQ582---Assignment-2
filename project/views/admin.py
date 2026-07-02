### import flask and blueprint / route template
from flask import Blueprint, render_template, flash, request, url_for, redirect, session, app
from project.db import user
from project.db.admin_db import get_access_requests, get_collection_items, get_user_role, get_item_by_id
from project.forms import RegisterCommunityElderForm, RegisterLibraryStaffForm, RegisterPublicForm, UpdateAccountForm, UpdateItemForm, UpdateRoleForm
from wtforms import form
from project.db.admin_db import get_collection_items, get_user_role
from project.db.user import add_public_user, add_library_staff, add_community_elder, email_exists
from project.forms import UpdateItemForm, UpdateRoleForm
from project.models.user import User
from ..db.setup import mysql
from ..wrappers import login_required, only_admins, only_staff
from hashlib import sha256

bp = Blueprint('admin', __name__)

#Route for the admin page
@bp.route('/admin', methods=['GET', 'POST'])
@login_required
@only_staff
def admin_dashboard():
    form = UpdateItemForm()
    db_items = get_collection_items()
    db_users = get_user_role()
    return render_template('admin.html', title='Admin', form=form, users=get_user_role(), items=get_collection_items(), requests=get_access_requests())

@bp.route('/admin/add_item', methods=['GET', 'POST'])
@login_required
@only_staff
def add_item():
    form = UpdateItemForm()
    if form.validate_on_submit():
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO collection_items (title, description, image_link, item_category, cultural_group, sensitivity_notes, review_status, access_level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (form.title.data, form.description.data, form.image_link.data.filename if form.image_link.data else None, form.item_category.data, form.cultural_group.data, form.sensitivity_notes.data, form.review_status.data, form.access_level.data))
        mysql.connection.commit()
        cur.close()
        flash('Item added successfully!', 'success')
        return redirect(url_for('admin.admin_dashboard'))
    return render_template('add_item.html', title='Add New Item', form=form)


@bp.route('/admin/manage_item/<int:item_id>', methods=['POST'])
@login_required
@only_admins
def manage_item(item_id):
    action = request.form.get('action')
    if action == 'delete':
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM collection_items WHERE item_id = %s", (item_id,))
        mysql.connection.commit()
        cur.close()
        flash('Item deleted successfully!', 'success')
    elif action == 'update':
        cur = mysql.connection.cursor()
        cur.execute("UPDATE collection_items SET title = %s, description = %s, image_link = %s, item_category = %s, cultural_group = %s, sensitivity_notes = %s, review_status = %s, access_level = %s WHERE item_id = %s", (request.form.get('title'), request.form.get('description'), request.form.get('image_link'), request.form.get('item_category'), request.form.get('cultural_group'), request.form.get('sensitivity_notes'), request.form.get('review_status'), request.form.get('access_level'), item_id))
        mysql.connection.commit()
        cur.close()
        flash('Item updated successfully!', 'success')
    return redirect(url_for('admin.admin_dashboard'))

@bp.route('/admin/edit_item/<int:item_id>', methods=['GET'])
@login_required
@only_staff
def edit_item(item_id):
    item = get_item_by_id(item_id)
    form = UpdateItemForm(data=item)
    return render_template('edit_item.html', title='Edit Item', form=form, item=item)

#===============Access Request Management ================

#@bp.route('/admin/manage_access_requests', methods=['GET', 'POST'])
#@login_required
#@only_admins
#def manage_access_requests():
#    if request.method == 'POST':
#        request_id = request.form.get('request_id')
#        new_status = request.form.get('new_status')
#        if request_id and new_status:
#            cur = mysql.connection.cursor()
#            cur.execute("UPDATE access_request SET request_status = %s WHERE request_id = %s", (new_status, request_id))
#            mysql.connection.commit()
#            cur.close()
#            flash('Access request status updated successfully!', 'success')
#        else:
#            flash('Invalid request ID or status.', 'error')
#    return render_template('admin_manage_access_requests.html', requests=get_access_requests(), title='Manage Access Requests')

@bp.route('/admin/update_access_request/<int:request_id>', methods=['GET', 'POST'])
@login_required
@only_admins
def update_access_request(request_id):
    new_status = request.form.get('new_status')
    if new_status:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE access_request SET request_status = %s WHERE request_id = %s", (new_status, request_id))
        mysql.connection.commit()
        cur.close()
        flash('Access request status updated successfully!', 'success')
    else:
        flash('Invalid status.', 'error')
    return redirect(url_for('admin.admin_dashboard', request_id=request_id))

@bp.route('/admin/view_access_request/<int:request_id>', methods=['GET'])
@login_required 
@only_admins
def view_access_request(request_id):
    return render_template('admin_view_access_request.html', request=get_access_requests(request_id), title='View Access Request')

#===============User Role Management ================

@bp.route('/admin/update_role/<int:user_id>', methods=['GET', 'POST'])
@login_required
@only_admins
def update_user_role(user_id):
    new_role = request.form.get('new_role')
    action = request.form.get('action')

    if new_role is not None:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE library_staff SET is_admin = %s WHERE user_ID = %s", (new_role, user_id))
        mysql.connection.commit()
        cur.close()
        flash('User role updated successfully!', 'success')
    elif action == 'delete':
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM library_staff WHERE user_ID = %s", (user_id,))
        mysql.connection.commit()
        cur.close()
        flash('User deleted successfully!', 'success')
    
    return redirect(url_for('admin.admin_dashboard'))

@bp.route('/admin/add_new_public_user', methods=['POST'])
@login_required
@only_staff
def add_new_public_user():
    form = RegisterPublicForm()
    if form.validate_on_submit():
        assert form.password.data, "Password is required"
        form.password.data = sha256(form.password.data.encode()).hexdigest() 
        if not email_exists(form.email.data):
            if add_public_user(form):
                flash('Public user added successfully!', 'success')
        else:
            flash('A user with that email already exists.', 'error')
            return redirect(url_for('admin.admin_dashboard'))
    else:
        flash('Please fill in all required fields.', 'error')
    return redirect(url_for('admin.admin_dashboard'))


@bp.route('/admin/add_new_library_staff', methods=['POST'])
@login_required
@only_admins
def add_new_library_staff():
    form = RegisterLibraryStaffForm()
    if form.validate_on_submit():
        assert form.password.data, "Password is required"
        form.password.data = sha256(form.password.data.encode()).hexdigest() 
        if not email_exists(form.email.data):
            if add_library_staff(form):
                flash('Library staff user added successfully!', 'success')
            else:
                flash('A user with that email already exists.', 'error')
                return redirect(url_for('admin.add_new_library_staff'))
    else:
        flash('Please fill in all required fields.', 'error')
    return redirect(url_for('admin.admin_dashboard'))

@bp.route('/admin/add_new_community_elder', methods=['POST'])
@login_required
@only_admins
def add_new_community_elder():
    form = RegisterCommunityElderForm()
    if form.validate_on_submit():
        assert form.password.data, "Password is required"
        form.password.data = sha256(form.password.data.encode()).hexdigest()
        if not email_exists(form.email.data):
            if add_community_elder(form):
                flash('Community elder user added successfully!', 'success')
            else:
                flash('A user with that email already exists.', 'error')
                return redirect(url_for('admin.add_new_community_elder'))
    else:
        flash('Please fill in all required fields.', 'error')
    return redirect(url_for('admin.admin_dashboard'))



# ================Account Page ================

@bp.route('/account/', methods=['GET', 'POST'])
@login_required
def update_account():
    form = UpdateAccountForm()
    user = session.get('user')
    if form.validate_on_submit():
        cur = mysql.connection.cursor()
        cur.execute("UPDATE user SET phone = %s, email = %s, password = %s WHERE id = %s", (form.phone.data, form.email.data, form.password.data, user['id']))
        mysql.connection.commit()
        cur.close()
        flash('Account updated successfully!', 'success')
        return redirect(url_for('admin.update_account'))
        
    return render_template('account.html', title='Update Account', form=form, user=user)


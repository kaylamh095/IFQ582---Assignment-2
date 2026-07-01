from datetime import date
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.fields import SubmitField, StringField, PasswordField, DateField, BooleanField, TextAreaField, FileField
from wtforms.validators import InputRequired, email, Length
from .models.public_user import PublicUser
from .models.library_staff import LibraryStaff
from .models.community_elder import CommunityElder


class LoginForm(FlaskForm):
    """Form for user login."""
    email = StringField("Email", validators = [InputRequired(), email()])
    password = PasswordField("Password", validators = [InputRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField("Login")


class RegisterPublicForm(FlaskForm):
    """Form for public user registration."""
    firstname = StringField("Your first name", validators = [InputRequired()])
    lastname = StringField("Your surname", validators = [InputRequired()])
    email = StringField("Email", validators = [InputRequired(), email()])
    phone = StringField("Your phone number", validators = [InputRequired(), Length(max=10)])
    password = PasswordField("Password", validators = [InputRequired()])
    submit = SubmitField("Make Account")


    def to_public_user(self) -> PublicUser:
        return PublicUser(
            first_name=self.firstname.data,
            last_name=self.lastname.data,
            email=self.email.data,
            phone=self.phone.data,
            password=self.password.data,
        )
    

class RegisterLibraryStaffForm(FlaskForm):
    """Form for library staff registration."""
    firstname = StringField("Your first name", validators = [InputRequired()])
    lastname = StringField("Your surname", validators = [InputRequired()])
    email = StringField("Email", validators = [InputRequired(), email()])
    phone = StringField("Your phone number", validators = [InputRequired(), Length(max=10)])
    password = PasswordField("Password", validators = [InputRequired()])
    position_title = StringField("Position title", validators = [InputRequired()])
    start_date = DateField("Start date", validators = [InputRequired()], default=date.today)
    is_admin = BooleanField("Is admin?", default=False)
    submit = SubmitField("Make Account")

    def to_library_staff(self) -> LibraryStaff:
        return LibraryStaff(
            first_name=self.firstname.data,
            last_name=self.lastname.data,
            email=self.email.data,
            phone=self.phone.data,
            password=self.password.data,
            position_title=self.position_title.data,
            start_date=self.start_date.data,
            is_admin=self.is_admin.data
        )
    

class RegisterCommunityElderForm(FlaskForm):
    """Form for library staff registration."""
    firstname = StringField("Your first name", validators = [InputRequired()])
    lastname = StringField("Your surname", validators = [InputRequired()])
    email = StringField("Email", validators = [InputRequired(), email()])
    phone = StringField("Your phone number", validators = [InputRequired(), Length(max=10)])
    password = PasswordField("Password", validators = [InputRequired()])
    community_name = StringField("Community name", validators = [InputRequired()])
    submit = SubmitField("Make Account")

    def to_community_elder(self) -> CommunityElder:
        return CommunityElder(
            first_name=self.firstname.data,
            last_name=self.lastname.data,
            email=self.email.data,
            phone=self.phone.data,
            password=self.password.data,
            community_name=self.community_name.data,
        )
    

# ============= CRUD Forms =============

class UpdateItemForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    image_link = FileField('Add an Image', validators=[FileAllowed(['jpg', 'png'])])
    item_category = StringField('Category', validators=[InputRequired()])
    cultural_group = StringField('Cultural Group', validators=[InputRequired()])
    sensitivity_notes = TextAreaField('Sensitivity Notes', validators=[InputRequired()])
    review_status = TextAreaField('Review Status', validators=[InputRequired()])
    access_level = StringField('Access Level', validators=[InputRequired()])
    submit = SubmitField('Submit')  

class UpdateAccountForm(FlaskForm):
    phone = StringField('Phone Number', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Update')
    
class UpdateRoleForm(FlaskForm):
    user_id = StringField('User ID', validators=[InputRequired()])
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), email()])
    role = StringField('Role', validators=[InputRequired()])
    submit = SubmitField('Update')

class UpdateAccessRequestForm(FlaskForm):
    request_id = StringField('Request ID', validators=[InputRequired()])
    user_id = StringField('User ID', validators=[InputRequired()])
    item_id = StringField('Item ID', validators=[InputRequired()])
    request_date = StringField('Request Date', validators=[InputRequired()])
    status = StringField('Status', validators=[InputRequired()])
    submit = SubmitField('Update')
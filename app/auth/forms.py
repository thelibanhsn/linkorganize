from ..extensions import FlaskForm, StringField, PasswordField, EmailField, SubmitField, FlaskForm, Length,data_required

class UserRegistrationForm(FlaskForm):
    first_name = StringField('First Name',validators=[data_required,Length(min=4, max=50)])
    last_name = StringField('Last Name',validators=[data_required,Length(min=4, max=50)])
    username = StringField('Username',validators=[data_required,Length(min=4, max=50)])
    email = EmailField('Email',validators=[data_required,Length(min=4, max=50)])
    password = PasswordField('Password',validators=[data_required,Length(min=4, max=32)])
    submit = SubmitField('Register')


class UserLoginForm(FlaskForm): 
    email = EmailField('Email',validators=[data_required,Length(min=4, max=50)])
    password = PasswordField('Password',validators=[data_required,Length(min=4, max=32)])
    submit = SubmitField('Login')


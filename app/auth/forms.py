from ..extensions import FlaskForm, StringField, PasswordField, EmailField, SubmitField, FlaskForm, Length,data_required, EqualTo

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

class ForgetPasswordForm(FlaskForm):
    email = EmailField('Registered Email',validators=[data_required,Length(min=4, max=50)])
    submit = SubmitField('Send OTP')


class OtpForm(FlaskForm):
    otp = StringField('OTP',validators=[data_required,Length(min=6, max=6)])
    submit = SubmitField('Verify OTP')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('New Password',validators=[data_required,Length(min=4, max=32), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Reset Password')


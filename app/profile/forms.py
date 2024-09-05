from ..extensions import FlaskForm, StringField, SubmitField, data_required,EmailField,PasswordField,Length


class ProfileUpdateForm(FlaskForm):
    first_name = StringField('First Name',validators=[data_required,Length(min=4, max=50)])
    last_name = StringField('Last Name',validators=[data_required,Length(min=4, max=50)])
    user_title = StringField('Title',validators=[data_required,Length(min=4, max=50)])
    user_bio = StringField('Bio',validators=[data_required,Length(min=4, max=255)])
    username = StringField('Username',validators=[data_required,Length(min=4, max=50)])
    email = EmailField('Email',validators=[data_required,Length(min=4, max=50)])
    submit = SubmitField('Update')
from ..extensions import FlaskForm, StringField, SubmitField, data_required,EmailField,FileField,Length, FileAllowed, FileRequired


class ProfileUpdateForm(FlaskForm):
    profile_pic = FileField('Upload Profile Pic',validators=[ FileAllowed(['png', 'jpg', 'jpeg', 'gif'], 'Images only!')])  
    first_name = StringField('First Name',validators=[data_required,Length(min=3, max=50)])
    last_name = StringField('Last Name',validators=[data_required,Length(min=3, max=50)])
    username = StringField('Username',validators=[data_required,Length(min=4, max=50)])
    email = EmailField('Email',validators=[data_required,Length(min=4, max=50)])
    user_title = StringField('Title',validators=[data_required,Length(min=3, max=50)])
    user_bio = StringField('Bio',validators=[data_required,Length(min=4, max=255)])
    submit = SubmitField('Update')
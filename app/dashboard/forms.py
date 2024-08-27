from ..extensions import StringField, SubmitField, SelectField, DataRequired


class AddLinkForm ():
    social_name = SelectField('Choose social media', choices=[('Instagram'), ('Twitter'), ('Facebook'), ('Youtube'), ('WhatsApp')], validators=[DataRequired])
    social_username = StringField('Username', validators=[DataRequired])
    submit = SubmitField('Add')
from ..extensions import StringField, SubmitField, SelectField, data_required, FlaskForm


class AddLinkForm (FlaskForm):
    social_name = SelectField('Choose social media', choices=[('Instagram'), ('X'), ('Facebook'), ('Youtube'), ('WhatsApp'), ('Snapchat'), ('Tiktok')], validators=[data_required])
    social_username = StringField('Username', validators=[data_required])
    submit = SubmitField('Add Link')
class UpdateLinkForm (FlaskForm):
    social_name = SelectField('Choose social media', choices=[('Instagram'), ('X'), ('Facebook'), ('Youtube'), ('WhatsApp'), ('Snapchat'), ('Tiktok')], validators=[data_required])
    social_username = StringField('Username', validators=[data_required])
    submit = SubmitField('Update Link')
class DeleteLinkForm (FlaskForm):
    social_name = SelectField('Choose social media', choices=[('Instagram'), ('X'), ('Facebook'), ('Youtube'), ('WhatsApp'), ('Snapchat'), ('Tiktok')], validators=[data_required])
    social_username = StringField('Username', validators=[data_required])
    submit = SubmitField('Delete Link')
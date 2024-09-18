from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_manager, UserMixin, current_user, login_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, EmailField, FileField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Length, EqualTo
from flask_migrate import Migrate
from flask_mail import Mail
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
mail = Mail()
data_required = DataRequired()
bootstrap = Bootstrap()
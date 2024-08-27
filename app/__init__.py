from flask import Flask
from .auth.routes import auth_bp
from .home.routes import home_bp
from .dashboard.routes import dashboard_bp
from .auth.models import User
from .extensions import login_manager, db, migrate, bootstrap

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    migrate.init_app(app, db)

    bootstrap.init_app(app)
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(dashboard_bp)
   

    return app

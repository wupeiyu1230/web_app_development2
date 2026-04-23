from flask import Blueprint

# Initialize Blueprints
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
main_bp = Blueprint('main', __name__)

# Import routes to register them with the blueprints
from app.routes import auth, main

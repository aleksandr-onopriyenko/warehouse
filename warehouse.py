from flask import Flask
from flask_cors import CORS
from models import db
from controllers import setup_routes


class Config:
    """Configuration class for the Flask application."""

    SQLALCHEMY_DATABASE_URI = "sqlite:///mydatabase.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration from the Config class
    CORS(app)  # Enable CORS for the app

    # Initialize the database with the app
    db.init_app(app)

    # Setup routes from controllers
    setup_routes(app)

    # Create database tables (run once)
    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()  # Create the app instance
    app.run(debug=True)

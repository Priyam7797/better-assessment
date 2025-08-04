from flask import Flask
from flask_cors import CORS
from models import db
from routes import comment_bp

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:5174", "http://localhost:5175"])
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.register_blueprint(comment_bp, url_prefix='/api')

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

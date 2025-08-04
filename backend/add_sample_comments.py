from app import create_app
from models import db, Comment

app = create_app()

with app.app_context():
    db.create_all()
    db.session.add(Comment(task_id=1, text='Sample comment 1'))
    db.session.add(Comment(task_id=1, text='Sample comment 2'))
    db.session.commit()

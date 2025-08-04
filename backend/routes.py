from flask import Blueprint, request, jsonify
from models import db, Comment

comment_bp = Blueprint('comments', __name__)

# GET comments for a specific task
@comment_bp.route('/comments/<int:task_id>', methods=['GET'])
def get_comments(task_id):
    comments = Comment.query.filter_by(task_id=task_id).all()
    return jsonify([
        {'id': c.id, 'task_id': c.task_id, 'text': c.text}
        for c in comments
    ])

# POST a new comment
@comment_bp.route('/comments', methods=['POST'])
def add_comment():
    data = request.get_json()
    if not data or 'task_id' not in data or 'text' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_comment = Comment(task_id=data['task_id'], text=data['text'])
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({
        'id': new_comment.id,
        'task_id': new_comment.task_id,
        'text': new_comment.text
    }), 201

# PUT to update an existing comment
@comment_bp.route('/comments/<int:id>', methods=['PUT'])
def edit_comment(id):
    data = request.get_json()
    comment = Comment.query.get_or_404(id)
    comment.text = data.get('text', comment.text)
    db.session.commit()
    return jsonify({'message': 'Comment updated'})

# DELETE a comment
@comment_bp.route('/comments/<int:id>', methods=['DELETE'])
def delete_comment(id):
    comment = Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    return jsonify({'message': 'Comment deleted'})

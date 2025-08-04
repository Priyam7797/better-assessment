import pytest
from app import create_app, db
from models import Comment

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_get_comments_empty(client):
    response = client.get('/api/comments/1')
    assert response.status_code == 200
    assert response.get_json() == []

def test_add_comment(client):
    response = client.post('/api/comments', json={'task_id': 1, 'text': 'Test comment'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['task_id'] == 1
    assert data['text'] == 'Test comment'

def test_get_comments(client):
    client.post('/api/comments', json={'task_id': 1, 'text': 'Test comment'})
    response = client.get('/api/comments/1')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['text'] == 'Test comment'

def test_edit_comment(client):
    post_resp = client.post('/api/comments', json={'task_id': 1, 'text': 'Old comment'})
    comment_id = post_resp.get_json()['id']
    put_resp = client.put(f'/api/comments/{comment_id}', json={'text': 'Updated comment'})
    assert put_resp.status_code == 200
    get_resp = client.get('/api/comments/1')
    data = get_resp.get_json()
    assert data[0]['text'] == 'Updated comment'

def test_delete_comment(client):
    post_resp = client.post('/api/comments', json={'task_id': 1, 'text': 'To be deleted'})
    comment_id = post_resp.get_json()['id']
    del_resp = client.delete(f'/api/comments/{comment_id}')
    assert del_resp.status_code == 200
    get_resp = client.get('/api/comments/1')
    data = get_resp.get_json()
    assert len(data) == 0

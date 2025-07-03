# backend/test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, GitHub Actions!"}

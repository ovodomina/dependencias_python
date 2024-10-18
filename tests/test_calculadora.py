import pytest
from app.routes import app
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))

from app.routes import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_somar(client):
    response = client.get('/somar?a=5&b=3')
    assert response.json['resultado'] == 8

def test_subtrair(client):
    response = client.get('/subtrair?a=5&b=3')
    assert response.json['resultado'] == 2

from apistar.test import TestClient
from app import app


def test_instant_answer_invalid_address():
    client = TestClient(app)
    response = client.get(
        url='http://localhost/v1/instant_answer',
        params={'q': 'azerty'}
    )

    assert response.status_code == 200
    assert response.json() == {
        'q': 'azerty',
        'is_address': False
    }


def test_instant_answer_bad_request():
    client = TestClient(app)
    response = client.get(
        url='http://localhost/v1/instant_answer'
    )

    assert response.status_code == 400
    assert response.json() == {
        'q': '"q" is required'
    }


def test_instant_answer_valid_address():
    client = TestClient(app)
    response = client.get(
        url='http://localhost/v1/instant_answer',
        params={'q': 'Rue de Rivoli Paris'}
    )

    assert response.status_code == 200
    assert response.json() == {
        'q': 'Rue de Rivoli Paris',
        'is_address': True
    }

def test_instant_answer_corporate():
    client = TestClient(app)
    response = client.get(
        url='http://localhost/v1/instant_answer',
        params={'q': 'Alwilda the legendary pirate 🏴‍☠️'}
    )

    assert response.status_code == 200
    assert response.json() == {
        'q': 'Alwilda the legendary pirate 🏴‍☠️',
        'is_address': False
    }

def test_instant_answer_with_emoji():
    client = TestClient(app)
    response = client.get(
        url='http://localhost/v1/instant_answer',
        params={'q': 'Fun with 🎌'}
    )

    assert response.status_code == 200
    assert response.json() == {
        'q': 'Fun with 🎌',
        'is_address': False
    }

def test_instant_answer_in_armenian_language():
    client = TestClient(app)
    response = client.get(
        url='http://localhost/v1/instant_answer',
        params={'q': 'Լիոնյան կայարան'}
    )

    assert response.status_code == 200
    assert response.json() == {
        'q': 'Լիոնյան կայարան',
        'is_address': False
    }

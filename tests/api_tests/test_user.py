from fastapi.testclient import TestClient
from config import settings
from main import app


client = TestClient(app)


def test_create_user():

    response = client.post(
        url='/user/create',
        json={
            'email': settings.TEST_USER_EMAIL,
            'password': settings.TEST_USER_PASSWORD})

    assert response.status_code == 200
    assert response.json() == {
        'error': False,
        'detail': 'User has successfully been created'}


def test_update_user():

    response = client.post(
        url='/user/update',
        json={
            'email': settings.TEST_USER_EMAIL,
            'password': settings.TEST_USER_PASSWORD,
            'is_active': settings.TEST_USER_STATUS})

    assert response.status_code == 200
    assert response.json() == {
        'error': False,
        'detail': 'User has successfully been updated'}

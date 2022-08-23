from fastapi.testclient import TestClient
from main import app


client = TestClient(app)
TEST_EMAIL = 'test@test.io'
TEST_PASSWORD = 'super-secret-password'
TEST_STATUS = False


def test_create_user():

    response = client.post(
        '/user/create',
        json={
            'email': TEST_EMAIL,
            'password': TEST_PASSWORD})

    assert response.status_code == 200
    assert response.json() == {
        'error': False,
        'detail': 'User has successfully been created'}


def test_update_user():

    response = client.post(
        '/user/update',
        json={
            'email': TEST_EMAIL,
            'password': TEST_PASSWORD,
            'is_active': TEST_STATUS})

    assert response.status_code == 200
    assert response.json() == {
        'error': False,
        'detail': 'User has successfully been updated'}

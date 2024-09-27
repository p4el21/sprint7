import allure
import pytest
import requests
from src.config import Config
from src.helpers import generate_random_user

@pytest.fixture
@allure.description('Создание нового курьера')
def create_courier():
    payload = generate_random_user()
    response = requests.post(f'{Config.URL}api/v1/courier', json=payload)
    assert response.status_code == 201, f'Ожидается статус: 201, получен статус: {response.status_code}'
    yield payload
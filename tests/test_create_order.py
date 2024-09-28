import pytest
import requests
from src.helpers import generate_random_order
from src.config import Config
import allure

class TestCreateOrder:
    @allure.title('Проверка создания заказа с выбором цвета самоката')
    @allure.description('Тест проверяет, что можно создать заказ с выбором цвета самоката')
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"]])
    def test_create_new_order_with_color(self, color):
        payload = generate_random_order()
        payload["color"] = color
        response = requests.post(f'{Config.URL}api/v1/orders', json=payload)
        assert response.status_code == 201, f'Ожидается статус: 201, получен статус: {response.status_code}'
        print(f' {response.status_code} {response.reason}. {response.text}')
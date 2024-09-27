import requests
from src.helpers import generate_random_order
from src.config import Config
import allure

class TestCreateOrder:
    @allure.description('Тест проверяет, что можно создать заказ с выбором цвета самоката')
    def test_create_new_order_with_color(self):
        payload = generate_random_order()
        payload["color"] = ["BLACK"]
        response = requests.post(f'{Config.URL}api/v1/orders', json=payload)
        assert response.status_code == 201, f'Ожидается статус: 201, получен статус: {response.status_code}'
        print(f' {response.status_code} {response.reason}. {response.text}')

    @allure.description('Тест проверяет, что можно создать заказ без выбора цвета самоката')
    def test_create_new_order_without_color(self):
        payload = generate_random_order()
        response = requests.post(f'{Config.URL}api/v1/orders', json=payload)
        assert response.status_code == 201, f'Ожидается статус: 201, получен статус: {response.status_code}'
        print(f' {response.status_code} {response.reason}. {response.text}')

    @allure.description('Тест проверяет, что можно создать заказ с выбором двух цветов самоката')
    def test_create_new_order_with_2_color(self):
        payload = generate_random_order()
        payload["color"] = ["BLACK", "GREY"]
        response = requests.post(f'{Config.URL}api/v1/orders', json=payload)
        assert response.status_code == 201, f'Ожидается статус: 201, получен статус: {response.status_code}'
        print(f' {response.status_code} {response.reason}. {response.text}')
import requests
from src.config import Config
import allure

class TestOrdersList:
    @allure.title('Проверка получения списка заказов')
    @allure.description('Тест на получение списка заказов')
    def test_get_orders_list(self):
        response = requests.get(f'{Config.URL}api/v1/orders')
        assert response.status_code == 200, f'Ожидается статус: 200, получен статус: {response.status_code}'
        print(f' {response.status_code} {response.reason}. {response.text}')

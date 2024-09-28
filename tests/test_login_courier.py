import pytest
import requests
from src.config import Config
import allure
from src.data import TextAnswers

class TestLoginCourier:
    @allure.title('Проверка авторизации курьера')
    @allure.description('Тест проверяет, что курьер может авторизоваться')
    def test_login_courier(self, create_courier):
        create_courier.pop("firstName")
        response = requests.post(f'{Config.URL}api/v1/courier/login', json=create_courier)
        assert response.status_code == 200, f'Ожидается статус: 200, получен статус: {response.status_code}'
        print(f' {response.status_code} {response.reason}. {response.text}')

    @allure.title('Проверка авторизации курьера без логина или пароля')
    @allure.description('Тест проверяет, что нельзя авторизоваться без логина или пароля')
    @pytest.mark.parametrize('login, password', [
        ('', 'password'),
        ('login', '')
    ])
    def test_login_courier_without_login(self, create_courier, login, password):
        create_courier.pop("firstName")
        create_courier['login'] = login
        create_courier['password'] = password
        response = requests.post(f'{Config.URL}api/v1/courier/login', json=create_courier)
        r = response.json()
        assert response.status_code == 400, f'Ожидается статус: 400, получен статус: {response.status_code}'
        assert r["message"] == TextAnswers.text400login, \
            f'Ожидается текст ответа: Недостаточно данных для входа, получен текст: {r["message"]}'
        print(f' {response.status_code} {response.reason}. {r["message"]}')

    @allure.title('Проверка авторизации курьера с несуществующими данными')
    @allure.description('Тест проверяет, что нельзя авторизоваться с несуществующими данными')
    def test_login_courier_with_non_existent_data(self):
        payload = {
            "login": '1111111',
            "password": 'pass',
            "firstName": 'Федор'
        }
        response = requests.post(f'{Config.URL}api/v1/courier/login', json=payload)
        r = response.json()
        assert response.status_code == 404, f'Ожидается статус: 404, получен статус: {response.status_code}'
        assert r["message"] == TextAnswers.text404login,\
            f'Ожидается текст ответа: Учетная запись не найдена, получен текст: {r["message"]}'
        print(f' {response.status_code} {response.reason}. {r["message"]}')



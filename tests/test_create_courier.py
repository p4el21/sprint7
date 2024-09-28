import pytest
import requests
from src.data import TextAnswers
from src.helpers import generate_random_user
from src.config import Config
import allure

class TestCreateCourier:
    @allure.title('Проверка создания курьера')
    @allure.description('Тест проверяет, что можно создать курьера')
    def test_create_new_courier(self):
        payload = generate_random_user()
        response = requests.post(f'{Config.URL}api/v1/courier', json=payload)
        assert response.status_code == 201, f'Ожидается статус: 201, получен статус: {response.status_code}'
        assert response.text == TextAnswers.text201create, f'Ожидается текст ответа: True, получен текст: {response.text}'
        print(f' {response.status_code} {response.reason}. {response.text}')

    @allure.title('Проверка создания курьера с существующими данными')
    @allure.description('Тест проверяет, что нельзя создать курьера с повторяющимися данными')
    def test_create_new_courier_with_existing_data(self):
        payload = {
            "login": 'Sergej',
            "password": 'pass',
            "firstName": 'Федор'
        }
        response = requests.post(f'{Config.URL}api/v1/courier', json=payload)
        r = response.json()
        assert response.status_code == 409, f'Ожидается статус: 409, получен статус: {response.status_code}'
        assert TextAnswers.text409create in r['message'], \
            f'Ожидается текст ответа: Этот логин уже используется, получен текст: {r["message"]}'
        print(f' {response.status_code} {response.reason}. {r["message"]}')

    @allure.title('Проверка создания курьера с существующим логином')
    @allure.description('Тест проверяет, что нельзя создать курьера с одним и тем же логином')
    def test_create_courier_with_existing_login(self):
        user_data = generate_random_user()
        payload = {
            "login": 'Sergej',
            "password": user_data['password'],
            "firstName": user_data['firstName']
        }
        response = requests.post(f'{Config.URL}api/v1/courier', json=payload)
        r = response.json()
        assert response.status_code == 409, f'Ожидается статус: 409, получен статус: {response.status_code}'
        assert TextAnswers.text409create in r['message'], \
            f'Ожидается текст ответа: Этот логин уже используется, получен текст: {r["message"]}'
        print(f' {response.status_code} {response.reason}. {r["message"]}')

    @allure.title('Проверка создания курьера без логина')
    @allure.description('Тест проверяет, что нельзя создать курьера без логина или пароля')
    @pytest.mark.parametrize('login, password', [('', 'password',),('login', '')])
    def test_create_courier_without_login(self, login, password):
        user_data = generate_random_user()
        payload = {
            user_data['login']: "login",
            user_data['password']: "password",
            user_data['firstName']: "firstName"
        }
        response = requests.post(f'{Config.URL}api/v1/courier', json=payload)
        r = response.json()
        assert response.status_code == 400, f'Ожидается статус: 400, получен статус: {response.status_code}'
        assert r['message'] == TextAnswers.text400create,\
            f'Ожидается текст ответа: Недостаточно данных для создания учетной записи, получен текст: {r["message"]}'
        print(f' {response.status_code} {response.reason}. {r["message"]}')


    @allure.title('Проверка создания курьера без имени')
    @allure.description('Тест проверяет, что можно создать курьера без имени')
    def test_create_courier_without_firstname(self):
        user_data = generate_random_user()
        payload = {
            "login": user_data['login'],
            "password": user_data['password']
        }
        response = requests.post(f'{Config.URL}api/v1/courier', json=payload)
        assert response.status_code == 201, f'Ожидается статус: 201, получен статус: {response.status_code}'
        assert response.text == TextAnswers.text201create, f'Ожидается текст ответа: True, получен текст: {response.text}'
        print(f' {response.status_code} {response.reason}. {response.text}')


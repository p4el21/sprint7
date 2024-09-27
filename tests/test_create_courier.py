import requests
from src.helpers import generate_random_user
from src.config import Config
import allure

class TestCreateCourier:
    @allure.description('Тест проверяет, что можно создать курьера')
    def test_create_new_courier(self):
        payload = generate_random_user()
        response = requests.post(f'{Config.URL}api/v1/courier', json=payload)
        assert response.status_code == 201, f'Ожидается статус: 201, получен статус: {response.status_code}'
        assert response.text == '{"ok":true}', f'Ожидается текст ответа: True, получен текст: {response.text}'
        print(f' {response.status_code} {response.reason}. {response.text}')

    @allure.description('Тест проверяет, что можно создать курьера с определенными данными')
    def test_create_new_courier_with_data(self):
        payload = {
            "login": 'Sergej',
            "password": 'pass',
            "firstName": 'Федор'
        }
        response = requests.post(f'{Config.URL}api/v1/courier', json=payload)
        assert response.status_code == 201, f'Ожидается статус: 201, получен статус: {response.status_code}'
        assert response.text == '{"ok":true}', f'Ожидается текст ответа: True, получен текст: {response.text}'
        print(f' {response.status_code} {response.reason}. {response.text}')

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
        assert r['message'] == "Этот логин уже используется.", \
            f'Ожидается текст ответа: Этот логин уже используется, получен текст: {r['message']}'
        print(f' {response.status_code} {response.reason}. {r['message']}')

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
        assert r['message'] == "Этот логин уже используется.", \
            f'Ожидается текст ответа: Этот логин уже используется, получен текст: {r['message']}'
        print(f' {response.status_code} {response.reason}. {r['message']}')

    @allure.description('Тест проверяет, что нельзя создать курьера без логина')
    def test_create_courier_without_login(self):
        user_data = generate_random_user()
        payload = {
            "password": user_data['password'],
            "firstName": user_data['firstName']
        }
        response = requests.post(f'{Config.URL}api/v1/courier', json=payload)
        r = response.json()
        assert response.status_code == 400, f'Ожидается статус: 400, получен статус: {response.status_code}'
        assert r['message'] == "Недостаточно данных для создания учетной записи",\
            f'Ожидается текст ответа: Недостаточно данных для создания учетной записи, получен текст: {r['message']}'
        print(f' {response.status_code} {response.reason}. {r['message']}')

    @allure.description('Тест проверяет, что нельзя создать курьера без пароля')
    def test_create_courier_without_password(self):
        user_data = generate_random_user()
        payload = {
            "login": user_data['login'],
            "firstName": user_data['firstName']
        }
        response = requests.post(f'{Config.URL}api/v1/courier', json=payload)
        r = response.json()
        assert response.status_code == 400, f'Ожидается статус: 400, получен статус: {response.status_code}'
        assert r['message'] == "Недостаточно данных для создания учетной записи",\
            f'Ожидается текст ответа: Недостаточно данных для создания учетной записи, получен текст: {r['message']}'
        print(f' {response.status_code} {response.reason}. {r['message']}')


    @allure.description('Тест проверяет, что нельзя создать курьера без имени')
    def test_create_courier_without_firstname(self):
        user_data = generate_random_user()
        payload = {
            "login": user_data['login'],
            "password": user_data['password']
        }
        response = requests.post(f'{Config.URL}api/v1/courier', json=payload)
        r = response.json()
        assert response.status_code == 400, f'Ожидается статус: 400, получен статус: {response.status_code}'
        assert r['message'] == "Недостаточно данных для создания учетной записи",\
            f'Ожидается текст ответа: Недостаточно данных для создания учетной записи, получен текст: {r['message']}'
        print(f' {response.status_code} {response.reason}. {r['message']}')


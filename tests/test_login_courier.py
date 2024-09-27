import requests
from src.config import Config
import allure

class TestLoginCourier:

    @allure.description('Тест проверяет, что курьер может авторизоваться')
    def test_login_courier(self, create_courier):
        login = create_courier['login']
        password = create_courier['password']
        auth_payload = {'login': login,
                   'password': password}
        response = requests.post(f'{Config.URL}api/v1/courier/login', json=auth_payload)
        assert response.status_code == 200, f'Ожидается статус: 200, получен статус: {response.status_code}'
        print(f' {response.status_code} {response.reason}. {response.text}')

    @allure.description('Тест проверяет, что нельзя авторизоваться без логина')
    def test_login_courier_without_login(self, create_courier):
        login = ''
        password = create_courier['password']
        auth_payload = {'login': login,
                        'password': password}
        response = requests.post(f'{Config.URL}api/v1/courier/login', json=auth_payload)
        r = response.json()
        assert response.status_code == 400, f'Ожидается статус: 400, получен статус: {response.status_code}'
        assert r['message'] == "Недостаточно данных для входа", \
            f'Ожидается текст ответа: Недостаточно данных для входа, получен текст: {r['message']}'
        print(f' {response.status_code} {response.reason}. {r['message']}')

    @allure.description('Тест проверяет, что нельзя авторизоваться без пароля')
    def test_login_courier_without_password(self, create_courier):
        login = create_courier['login']
        password = ''
        auth_payload = {'login': login,
                   'password': password}
        response = requests.post(f'{Config.URL}api/v1/courier/login', json=auth_payload)
        r = response.json()
        assert response.status_code == 400, f'Ожидается статус: 400, получен статус: {response.status_code}'
        assert r['message'] == "Недостаточно данных для входа",\
            f'Ожидается текст ответа: Недостаточно данных для входа, получен текст: {r['message']}'
        print(f' {response.status_code} {response.reason}. {r['message']}')

    @allure.description('Тест проверяет, что нельзя авторизоваться с несуществующими данными')
    def test_login_courier_with_non_existent_data(self):
        payload = {
            "login": '111111',
            "password": 'pass',
            "firstName": 'Федор'
        }
        response = requests.post(f'{Config.URL}api/v1/courier/login', json=payload)
        r = response.json()
        assert response.status_code == 404, f'Ожидается статус: 404, получен статус: {response.status_code}'
        assert r['message'] == "Учетная запись не найдена",\
            f'Ожидается текст ответа: Учетная запись не найдена, получен текст: {r['message']}'
        print(f' {response.status_code} {response.reason}. {r['message']}')



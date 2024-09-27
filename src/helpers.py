import random
from faker import Faker

def generate_random_user():
    fake = Faker('ru_RU')
    user = {
        "login": fake.user_name(),
        "password": fake.password(),
        "firstName": fake.first_name(),
    }
    return user

def generate_random_order():
    fake = Faker('ru_RU')
    user = {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": fake.city(),
        "phone": fake.phone_number(),
        "rentTime":random.randint(1, 30),
        "deliveryDate": fake.date_between(start_date='today', end_date='+30d').isoformat(),
        "comment":fake.sentence(),
    }
    return user
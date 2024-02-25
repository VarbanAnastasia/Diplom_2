import json
from faker import Faker

faker = Faker()


class PayloadCreateUser:
    headers_unique = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY1ZGFkODAzOWVkMjgwMDAxYjNiZDgwZSIsImlhdCI6MTcwODg0MDk3NSwiZXhwIjoxNzA4ODQyMTc1fQ.L_leEDpsto8PSxknRbhLR3PURY9ljcc9GFr9xhZnG8U'
    }

    create_user_200_payload = json.dumps({
        "email": faker.email(),
        "password": faker.password(),
        "name": faker.name()
    })
    create_user_one_missing = json.dumps({
        "email": faker.email(),
        "password": faker.password()
    })
    create_user_existed = json.dumps({
        "email": "avarban@mail.ru",
        "password": "123456789QWERTY",
        "name": "Anastasia"
    })


class PayloadLoginUser:
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY1ZGFkODAzOWVkMjgwMDAxYjNiZDgwZSIsImlhdCI6MTcwODg0MDk3NSwiZXhwIjoxNzA4ODQyMTc1fQ.L_leEDpsto8PSxknRbhLR3PURY9ljcc9GFr9xhZnG8U'
    }

    login_user_existed = json.dumps({
        "email": "avarban@mail.ru",
        "password": "123456789QWERTY",
        "name": "Anastasia"
    })
    login_wrong_data = json.dumps({
        "email": faker.email(),
        "password": faker.password(),
        "name": faker.name()
    })

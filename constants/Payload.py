import json
from faker import Faker

faker = Faker()


class PayloadCreateUser:
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


class PayloadChangeData:
    user = json.dumps({
        "email": "avarban@mail.ru",
        "password": "123456789QWERTY",
        "name": "Anastasia"
    })

    user_changed_data = {
        "email": "avarban@mail.ru",
        "password": "123456789QWERTY",
        "name": "Nastya"
    }

    data_double = {
        "email": "abvarban@mail.ru",
        "password": faker.password(),
        "name": faker.name()
    }


class IngredientsPayload:
    data_ingredient = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    }

    data_not_ingredient = {
        "ingredients": []
    }

    data_bad_ingredient = {
        "ingredients": ["61c0c5a71d1f82001bdaaa61", "61c0c5a71d1f82001bdaaa61"]
    }

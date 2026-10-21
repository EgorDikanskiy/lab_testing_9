import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_user():
    response = requests.get(BASE_URL + "/users/1")

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    user = response.json()
    # структура ответа
    for field in ["id", "name", "username", "email", "address", "phone", "website", "company"]:
        assert field in user
    assert "city" in user["address"]
    assert "name" in user["company"]
    # типы полей
    assert isinstance(user["id"], int)
    assert isinstance(user["name"], str)
    assert isinstance(user["email"], str)
    # значения
    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"
    assert user["email"] == "Sincere@april.biz"


def test_create_user():
    new_user = {"name": "Egor Dikanskiy", "username": "egor", "email": "egor@example.com"}

    response = requests.post(BASE_URL + "/users", json=new_user)

    assert response.status_code == 201

    user = response.json()
    assert set(user.keys()) == {"id", "name", "username", "email"}
    assert isinstance(user["id"], int)
    assert user["name"] == new_user["name"]
    assert user["username"] == new_user["username"]
    assert user["email"] == new_user["email"]
    # в базе 10 пользователей, поэтому новый получает id = 11
    assert user["id"] == 11


def test_update_user():
    updated_user = {"name": "Egor Updated", "username": "egor_new", "email": "egor.new@example.com"}

    response = requests.put(BASE_URL + "/users/1", json=updated_user)

    assert response.status_code == 200

    user = response.json()
    assert set(user.keys()) == {"id", "name", "username", "email"}
    assert user["id"] == 1
    assert user["name"] == updated_user["name"]
    assert user["username"] == updated_user["username"]
    assert user["email"] == updated_user["email"]

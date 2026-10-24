from app import app, add


def test_add():
    assert add(2, 3) == 5


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Hello from Basic CI app"


def test_add_route():
    client = app.test_client()
    response = client.get("/add/4/6")
    assert response.get_json()["result"] == 10
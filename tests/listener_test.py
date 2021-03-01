import requests


def test_listener_add_success():
    response = requests.post(
        "http://localhost:8000/listener/", data={"action": "listener_add"}
    )
    assert response.status_code == 200

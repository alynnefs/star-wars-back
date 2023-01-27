import pytest
from app.main import app


@pytest.fixture()
def app_test():
    app_test = app
    app_test.config.update(
        {
            "TESTING": True,
        }
    )

    yield app_test


@pytest.fixture()
def client(app_test):
    return app_test.test_client()


def test_request_slash(client):
    response = client.get("/")

    # This route doesn't exist
    assert b"404 Not Found" in response.data

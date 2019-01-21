import pytest

from flask import Flask

from server import app


@pytest.fixture
def client():

    return app.test_client()


def test_request(client):

    resp = client.get("/")
    assert resp.status_code == 200


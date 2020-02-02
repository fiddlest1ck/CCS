import pytest
from flask import Response
from server import server


@pytest.fixture
def app():
    yield server


@pytest.fixture
def client(app):
    return server.test_client()

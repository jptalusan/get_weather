import pytest
from api_key_package.client import dummy_api_call
import os

def test_dummy_api_call(monkeypatch):
    monkeypatch.setenv("API_KEY", "testkey123")
    assert dummy_api_call() == "Calling API with key: test****"

"""Test module for main"""
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

print("Am I even running")

def test_echo_message():
    """Test that foo is echoed"""
    response = client.get("/echo/foo")
    assert str(response.text).find('Your message: "foo"')

def test_echo_number():
    """Test that bar is also echoed"""
    response = client.get("/echo/bar")
    assert str(response.text).find('Your message: "bar"')

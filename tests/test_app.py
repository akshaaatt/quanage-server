"""Imports"""
from flask import Flask

def test_base_route():
    """Comments"""
    app = Flask(__name__)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'Hi Qiskitter!'
    assert response.status_code == 200

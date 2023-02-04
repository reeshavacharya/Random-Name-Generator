import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from namegetter import nameGetter
from main import app, generate_name
from fastapi.exceptions import HTTPException


@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def namegetter():
    return nameGetter()

def test_generate_name(client, namegetter):
    with patch.object(nameGetter, 'get_name', return_value="ram") as mock_get_name:
        response = client.get('/name/', params={'gender': 'male', 'country': 'nepal'})
        assert response.status_code == 200
        assert response.json() == "ram"
        mock_get_name.assert_called_with('male', 'nepal')
        
def test_generate_name_without_params(client, namegetter):
    with patch.object(nameGetter, 'get_name', return_value="sita") as mock_get_name:
        response = client.get('/name/')
        assert response.status_code == 200
        assert response.json() == "sita"
        mock_get_name.assert_called_with(None, None)

def test_generate_name_404_error(client, namegetter):
    with patch.object(nameGetter, 'get_name', side_effect=HTTPException(status_code=404)) as mock_get_name:
        response = client.get('/name/', params={'gender': 'male', 'country': 'us'})
        assert response.status_code == 404
        assert response.json() == {"detail": "Not Found"}

def test_generate_name_500_error(client, namegetter):
    with patch.object(nameGetter, 'get_name', side_effect=HTTPException(status_code=500)) as mock_get_name:
        response = client.get('/name/', params={'gender': 'male', 'country': 'us'})
        assert response.status_code == 500
        assert response.json() == {"detail": "Internal Server Error"}

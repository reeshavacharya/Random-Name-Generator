import pytest
from unittest.mock import patch, MagicMock
from namegetter import nameGetter
from main import app, generate_name
from fastapi.exceptions import HTTPException

@pytest.fixture
def Get_Names():
    return nameGetter()

def test_generate_name(Get_Names):
    with patch.object(nameGetter, 'get_name', return_value="ram") as mock_get_name:
        result = generate_name(gender='male', country='nepal')
        assert result == "ram"
        mock_get_name.assert_called_with('male', 'nepal')

def test_generate_name_without_params(Get_Names):
    with patch.object(nameGetter, 'get_name', return_value="ram") as mock_get_name:
        result = generate_name(gender=None, country=None)
        assert result == "ram"
        mock_get_name.assert_called_with(None, None)

def test_generate_name_404_error(Get_Names):
    with patch.object(nameGetter, 'get_name', side_effect=HTTPException(status_code=404)):
        with pytest.raises(HTTPException) as e:
            generate_name(gender='male', country='nepal')
        assert e.value.status_code == 404

def test_generate_name_500_error(Get_Names):
    with patch.object(nameGetter, 'get_name', side_effect=HTTPException(status_code=500)):
        with pytest.raises(HTTPException) as e:
            generate_name(gender='male', country='nepal')
        assert e.value.status_code == 500
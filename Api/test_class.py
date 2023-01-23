import pytest
from namegetter import nameGetter
from unittest.mock import Mock, patch
import csv

@pytest.fixture
def nameGet():
    return nameGetter()

@patch('requests.get')
def test_get_name(mock_get):
    flag=False
    name=nameGetter.get_name("male")
    with open('./data.csv', 'r') as file:
        reader= csv.reader(file)
        next(reader)
        for row in reader:
            if(row[1]=="male"):
                if name==row[0]:
                    flag=True
    assert flag==True

@patch('requests.get')
def test_get_name_with_country(mock_get):
    flag=False
    name= nameGetter.get_name_with_country("male", "nepal")
    with open('./data.csv','r') as file:
        reader= csv.reader(file)
        next(reader)
        for row in reader:
            if(row[1]=="male" and row[2]=="nepal" and name==row[0]):
                flag=True
    assert flag==True



    


    

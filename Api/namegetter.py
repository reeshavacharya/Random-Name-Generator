import csv
from os.path import abspath, join, dirname
from random import choice
import pandas as pd

def get_name(gender= None):
    data=pd.read_csv('data.csv')
    filteredData=[]
    if(gender==None):
       for index, row in data.iterrows():
          filteredData.append(row['name'])
       return choice(filteredData)
    else:   
     gender_lower=gender.lower()
     for index, row in data.iterrows():
         if row['gender']==gender_lower:
             filteredData.append(row['name'])
     return choice(filteredData) 

def get_name_with_country(gender=None, country=None):
    filteredData=[]
    country_lower=country.lower()  
    if(gender==None): 
        with open('data.csv', 'r') as file:
            reader= csv.reader(file)
            next(reader)
            for row in reader:
                if(row[2]==country_lower):
                    filteredData.append(row[0])
        return choice(filteredData)
    else:       
        gender_lower=gender.lower()
        with open('data.csv', 'r') as file:
            reader= csv.reader(file)
            next(reader)
            for row in reader:
                if(row[1]==gender_lower and row[2]==country_lower):
                    filteredData.append(row[0])
        return choice(filteredData)
    
def get_name_withoutGender(country):
   filteredData=[]
   country_lower=country.lower()
   with open('data.csv', 'r') as file:
    reader= csv.reader(file)
    next(reader)
    for row in reader:
        if(row[2]==country_lower):
            filteredData.append(row[0])
   return choice(filteredData) 
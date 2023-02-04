import csv
from random import choice

class nameGetter:    
    def get_name(gender: str = None, country: str = None):
        names = []
        with open('data.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if (row['gender'] == gender or gender is None) and (row['country'] == country or country is None):
                    names.append(row['name'])
        return choice(names)           
                
                

            
    
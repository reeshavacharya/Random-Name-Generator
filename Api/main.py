from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from namegetter import nameGetter
import countries
import genders

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/name")
async def generate_name():
 name= nameGetter.get_name(None)
 return name  

@app.get("/name/{gender}")
async def generate_name(gender):
    name= nameGetter.get_name(gender)
    return name  

@app.get("/name/{gender}/{country}")
async def generate_name(gender,country):   
        name= nameGetter.get_name_with_country(gender,country)
        return name
     

@app.get("/countries")
async def generate_countries():
   countryList= countries.countryList()
   return countryList

@app.get("/genders")
async def generate_genders():
   genderList= genders.genderList()
   return genderList


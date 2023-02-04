from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException
from namegetter import nameGetter
import countries
import genders

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/name/')
def generate_name(gender: str = Query(None, alias="gender"), country: str = Query(None, alias="country")):
    try:
        name=nameGetter.get_name(gender,country)
        return name 
    except HTTPException as e:
        raise e

@app.get("/countries")
async def generate_countries():
   try:
    countryList= countries.countryList()
    return countryList
   except HTTPException as e:
        raise e

@app.get("/genders")
async def generate_genders():
   try:
    genderList= genders.genderList()
    return genderList
   except HTTPException as e:
        raise e 

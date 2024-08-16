from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from mlmodel import rec_system
import os
from dotenv import load_dotenv, find_dotenv
import pymysql

load_dotenv(find_dotenv())

# KEYS
HOST = os.environ.get("HOST")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
DATABASE = os.environ.get("DATABASE")
PORT = os.environ.get("PORT")


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

class User(BaseModel):
    email: str
    password: str


# # # Iniciar la Conexion
def star_connection():
    try:
        connect = pymysql.connect(
            host="localhost",
            user= "root",
            password="Joan92",
            database="dataForge",
            # port= PORT
        )
        query = """CREATE TABLE IF NOT EXISTS cities(
            idcity INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
            city VARCHAR(50))"""
        cursor = connect.cursor()
        cursor.execute(query)
        connect.commit()
        print("SUCCESS...")
        return connect
    except Exception:
        print("Not Available")


def get_city(texto):
    city = rec_system(texto)
    connect = star_connection()
    query = f"INSERT INTO cities (city) VALUES ('{city}')"
    cursor = connect.cursor()
    cursor.execute(query)
    connect.commit()
    connect.close()
    return city

def get_data():
    connect = star_connection()
    cursor = connect.cursor()
    cursor.execute("SELECT CITY ,COUNT(*) AS cant FROM cities GROUP BY city ORDER BY cant DESC")
    cities = cursor.fetchall()
    connect.close()
    return cities



@app.get("/")
async def login(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/destinos")
async def destiny(request: Request):
    return templates.TemplateResponse("destinos.html",{"request":request})
@app.get("/admin")
async def admin(request: Request):
    return templates.TemplateResponse("admin.html",{"request":request})

@app.post("/destinos")
async def destiny( request : Request,descripcion:str=Form(...)):
    place = get_city(descripcion)
    city= place.iloc[0]["city"].replace(" ","+")
    state= place.iloc[0]["state"]
    if(city!="error"):
        return templates.TemplateResponse("destinos.html",{"request":request,"city":city,"state":state})
    else:
        return templates.TemplateResponse("destinos.html",{"request":request})




@app.post("/admin")
async def login_post(request:Request,email:str= Form(...), password: str=Form(...)):
    if(email=="admin@admin.com" and password=="password"):
        cities= get_data()
        return templates.TemplateResponse("stats.html",{"request":request, "cities":cities})
    else:
        return templates.TemplateResponse("admin.html",{"request":request})
    
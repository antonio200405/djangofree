from fastapi import FastAPI
import mysql.connector
import json
from database import *
from pydantic import BaseModel
from routers import currency




app = FastAPI()


@app.on_event("startup")
async def startup():
    if conn.is_closed():
        conn.connect()


@app.on_event("shutdown")
async def shutdown():
    print("Closing...")
    if not conn.is_closed():
        conn.close()




@app.get("/")
async def root():
    return {"message": "Currency application"}


app.include_router(currency.router_currency)
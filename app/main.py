# app/main.py
from typing import Optional

from contextlib import asynccontextmanager
from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database import engine, SessionLocal
from app.models import Base
from app.schemas import Customer, Order

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup (dev/exam). Prefer Alembic in production.
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)

def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()


# ---- Health ----
@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/api/customer")
def post_customer(customer: customer):
    return customer

@app.get("/api/customer")
def customer():
    return {"Customer List": }

@app.get("/api/customer/{id}")
def get_customer(id: int):
    return {"Customer ID": id}  

@app.put("/api/customer/{id}")
def put_customer():
    return {"Customer Updated": }  

@app.patch("/api/customer/{id}")  
def patch_customer():
    return {"Customer Partially Updated": }  

@app.delete("/api/customer/{id}") 
def delete_customer():
    return {"Customer Deleted": }  

@app.post("/api/order")
def post_order(order: order):
    return order

@app.get("/api/order")
def order():
    return {"Order List": }

@app.get("/api/order/{id}")
def get_order(id: int):
    return {"Order ID": id}

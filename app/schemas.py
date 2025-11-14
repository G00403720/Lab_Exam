from typing import Annotated, Optional
from pydantic import BaseModel, EmailStr, Field, StringConstraints, ConfigDict, constr

class Customer(BaseModel):
    id: int
    name: constr(min_length=1, max_length=100) 
    email: EmailStr
    customer_since: constr(min_length=2000, max_length=2100)

class Order(BaseModel):
    id: int
    order_number: constr(min_length=3, max_length=20)
    total_cents: constr(min_length=1, max_length=1000000)   
    customer_id: int
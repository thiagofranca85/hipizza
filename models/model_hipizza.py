from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    name: str = Field(index=True)
    email: str = Field(index=True)
    phone: int = Field(index=True)
    whatsapp: Optional[bool] = Field(index=True)
    password: str = Field(index=True)
    address: str = Field(index=True)
    

class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    name: str = Field(nullable=False, index=True)
    price: float = Field(nullable=False, index=True)
    description: str = Field()
    
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
      

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    status: str = Field(index=True)
    shipping_value: float = Field(index=True)
    payment_method: str = Field(index=True)
    order_date: datetime = Field(index=True)
    total_price: float = Field(index=True)

    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

    item_id: Optional[int] = Field(default=None, foreign_key="item.id")



class Order_Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    quantity: int = Field(index=True)
    price: float = Field(index=True)

    item_id: Optional[int] = Field(default=None, foreign_key="item.id")

    order_id: Optional[int] = Field(default=None, foreign_key="order.id")





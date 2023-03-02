from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from time import datetime


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    name: str = Field(index=True)
    email: str = Field(index=True)
    phone: int = Field(index=True)
    whatsapp: bool = Field(index=True)
    password: str = Field(index=True)
    address: str = Field(index=True)
    
    students: List["Student"] = Relationship(back_populates="classroom")
    groups: List["Group"] = Relationship(back_populates="classroom")
   


class Menu(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    name: str = Field(nullable=False, index=True)
    price: float = Field(nullable=False, index=True)
    description: str = Field()
    
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="users")
    
    students: List["Student"] = Relationship(back_populates="group")

    
    

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    status: str = Field(index=True)
    shipping_value: float = Field(index=True)
    payment_method: str = Field(index=True)
    order_date: datetime = Field(index=True)
    total_price: float = Field(index=True)

    id_classroom: Optional[int] = Field(default=None, foreign_key="classroom.id")
    classroom: Optional[ClassRoom] = Relationship(back_populates="students")

    id_group: Optional[int] = Field(default=None, foreign_key="group.id")
    group: List["Group"] = Relationship(back_populates="students")


class Order_Menu(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    quantity: int = Field(index=True)
    price: float = Field(index=True)

    id_classroom: Optional[int] = Field(default=None, foreign_key="classroom.id")
    classroom: Optional[ClassRoom] = Relationship(back_populates="students")

    id_group: Optional[int] = Field(default=None, foreign_key="group.id")
    group: List["Group"] = Relationship(back_populates="students")




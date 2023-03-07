from fastapi import APIRouter
from main import app

from routes import user_routes
from routes import item_routes
from routes import order_routes
from routes import auth

app.include_router(user_routes.router)
app.include_router(item_routes.router)
app.include_router(order_routes.router)
app.include_router(auth.router)
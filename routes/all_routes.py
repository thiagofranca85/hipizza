# from fastapi import APIRouter

# from routes import classroom_routes
# from routes import students_routes
# from routes import groups_routes

# from main import app

# app.include_router(classroom_routes.router)
# app.include_router(groups_routes.router)
# app.include_router(students_routes.router)

from fastapi import APIRouter
from main import app

from routes import user_routes
from routes import item_routes
from routes import order_routes

app.include_router(user_routes.router)
app.include_router(item_routes.router)
app.include_router(order_routes.router)

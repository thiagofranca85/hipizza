# from database import engine
# from models.model import ClassRoom

# from sqlmodel import Session
# from sqlmodel import select

# from sqlalchemy.orm import selectinload

# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import JSONResponse

# from models.model import Student
# from typing import Optional, List


# from fastapi import Response
# import json
# from fastapi import HTTPException, status


# ### Cadastrar uma sala/classe
# # Isso é apenas um ex, ainda não está pronto
# def cadastraClasse(classRoom:ClassRoom):
#     with Session(engine) as session:
#         new_class = ClassRoom(id=None, name=classRoom.name)
#         session.add(new_class)
#         session.commit()
#         session.refresh(new_class)
#         return new_class


# def buscaClasseAlunos(classeID: int = None):

#     with Session(engine) as session:
#         if classeID is None:
#             statement = select(ClassRoom).options(selectinload(ClassRoom.students))
#             results = session.exec(statement).all()
#             if not results:
#                 raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                     detail = {"message": f"No Class found with id: {classeID}"}
#                 )
#             else:
#                 return results
            
#         else:
#             statement = select(Student).where(Student.id_classroom == classeID)
#             results = session.exec(statement).all()
#             if not results:
#                 raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                     detail = {"message": f"No Class found with id: {classeID}"}
#                 )
#             else:
#                 return results            

    
# def createClass(classRoom:ClassRoom):
#     with Session(engine) as session:
#         new_class = ClassRoom(id=None, name=classRoom.name)
#         session.add(new_class)
#         session.commit()
#         session.refresh(new_class)
#         return new_class
    
# def editClass(classID, classRoom:ClassRoom):
#     with Session(engine) as session:
#         statement = select(ClassRoom).where(ClassRoom.id == classID)
#         results = session.exec(statement).first()
        
#         if not results:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                 detail = {"message": f"No Class found with id {classID}"}
#             )
#         else:
#             results.name = classRoom.name

#             session.add(results)
#             session.commit()
#             session.refresh(results)
#             print(results)
#             return JSONResponse(content=jsonable_encoder(results))

# def deleteClass(classID):
#     with Session(engine) as session:
#         statement = select(ClassRoom).where(ClassRoom.id == classID)
#         results = session.exec(statement).first()
#         if not results:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                 detail = {"message": f"No Class found with id: {classID}"}
#             )
#         else:
#             session.delete(results)
#             session.commit()
#             #Não sei exatamente o que retornar aqui
#             return True

from database import engine
from models.model_hipizza import Item

from sqlmodel import Session
from sqlmodel import select

from sqlalchemy.orm import selectinload

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import HTTPException, status
from fastapi import Response

from typing import Optional, List

import json


def allItems():
    with Session(engine) as session:
        statement = select(Item)
        
        results = session.exec(statement).all()
        # print(results)
        return results
    
def createItem(item:Item):
    with Session(engine) as session:
        new_item = Item(id=None, name=item.name, price=item.price, description=item.description)
        session.add(new_item)
        session.commit()
        session.refresh(new_item)
        return new_item
    
def editItem(itemID, item:Item):
    with Session(engine) as session:
        statement = select(Item).where(Item.id == itemID)
        results = session.exec(statement).first()
        results.name = item.name
        results.price = item.price
        results.description = item.description

        session.add(results)
        session.commit()
        session.refresh(results)
        print(results)
        return JSONResponse(content=jsonable_encoder(results))

def deleteItem(itemID):
    with Session(engine) as session:
        statement = select(Item).where(Item.id == itemID)
        results = session.exec(statement).first()
        session.delete(results)
        session.commit()
        return True
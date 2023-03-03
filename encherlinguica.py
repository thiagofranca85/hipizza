from database import engine
from sqlmodel import Session, select
from models.model import ClassRoom, Student, Group
from models.model_hipizza import User, Item, Order
from sqlalchemy.orm import selectinload

import random

def cadastraClass():
    with Session(engine) as session:
        new_class = ClassRoom(id=None, name=input("Nome da Classe: "))
        session.add(new_class)
        session.commit()
        #session.refresh(new_class)
        print(new_class)

def cadastrarUser():
    with Session(engine) as session:
        new_user = User(id=None, name=input("Nome: "),
                        email=input("Email: "),
                        phone=input("Telefone: "),
                        password=input("Senha: "),
                        address=input("Endereço: ")   
                        )
        session.add(new_user)
        session.commit()
        #session.refresh(new_user)
        print(new_user)

def cadastrarItem():
    with Session(engine) as session:
        new_item = Item(id=None, name=input("Nome: "),
                        price=input("Preço: "),
                        description=input("Descrição: ") 
                        )
        session.add(new_item)
        session.commit()
        #session.refresh(new_item)
        print(new_item)

def buscaUser(id):
    with Session(engine) as session:
        statement = select(User).where(User.id==id)
        
        results = session.exec(statement).first()
        print(results)
        return results
    
def buscaItem(id):
    with Session(engine) as session:
        statement = select(Item).where(Item.id==id)
        
        results = session.exec(statement).first()
        print(results)
        return results

def editUser(userID):
    with Session(engine) as session:
        statement = select(User).where(User.id == userID)
        results = session.exec(statement).first()
        
        # if not results:
        #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        #         detail = {"message": f"No Student found with id {userID}"}
        #     )
        # else:
        results.name = input("Novo Nome: ")

        session.add(results)
        session.commit()
        session.refresh(results)
        print(results)
            # return JSONResponse(content=jsonable_encoder(results))
        
def deleteUser(userID):
    with Session(engine) as session:
        statement = select(User).where(User.id == userID)
        results = session.exec(statement).first()
        # if not results:
        #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        #         detail = {"message": f"No Student found with id: {userID}"}
        #     )
        # else:
        session.delete(results)
        session.commit()
        print(f"Apagou o usuario com ID {userID}")
            #Não sei exatamente o que retornar aqui
        return True

def cadastrarGrupo(idClassRoom):
    with Session(engine) as session:
        new_class = Group(id=None, name=input("Nome do grupo: "), description=input("Descrição do grupo: "), id_classroom=idClassRoom)
        session.add(new_class)
        session.commit()
        #session.refresh(new_class)
        print(new_class)
        
def buscaClasseAlunos():
    with Session(engine) as session:
        statement = select(ClassRoom).options(selectinload(ClassRoom.students)).options(selectinload(ClassRoom.groups))
        
        results = session.exec(statement).all()
        print(results)
        return results
    
#TEste!!! altamente errado!
def enfiaAlunoNoGrupo(id_student, id_classe):
    with Session(engine) as session:
        statement1 = select(Student).where(Student.id == id_student)
        statement2 = select(Group).where(Group.id_classroom == id_classe)
        estudante = session.exec(statement1).first()
        grupos = session.exec(statement2).all()
        random.shuffle(grupos)
        estudante.id_group = grupos[0].id
        estudante.group = grupos[0]
        print("Primeiro grupo: "+str(grupos[0]))
        print ("Estudante: "+str(estudante))
        print("Grupos: "+str(grupos))
        session.add(estudante)
        session.commit()
        session.refresh(estudante)
        return estudante
        

def buscaGrupo():
    with Session(engine) as session:
        statement = select(Group).options(selectinload(Group.students))
        
        results = session.exec(statement).all()
        print(results)
        return results


# while True:
#     print("Escolha uma das opções: ")
#     print("\n 1 - Cadastrar Classe\n 2 - Cadastrar aluno\n 3 - Cadastrar Grupo\n 4 - Listar tudo\n Digite qualquer outro número para sair.\n")
#     match input(" > "):
#         case "1":
#             cadastraClass()
#         case "2":
#             cadastrarStudent(input("Informe o ID da sala: "))
#         case "3":
#             cadastrarGrupo(input("Informe o ID da sala: "))
#         case "4":
#             buscaClasseAlunos()
#         case _:
#             break


# enfiaAlunoNoGrupo(1,1)
# cadastrarUser()
# cadastrarItem()
# buscaUser(1)
# buscaItem(2)

# editUser(1)
deleteUser(1)
#buscaGrupo()
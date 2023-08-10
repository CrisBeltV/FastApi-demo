from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix= "/user", tags=['user'])

# uvicorn user:router --reload


class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    url: str = None


users_fic_list = [
    User(id=1, name="Jey", surname="Mon", age=33, url="https://jey.com"),
    User(id=2, name="Leo", surname="Cen", age=34, url="https://leo.com"),
    User(id=3, name="Aura", surname="Luc", age=36, url="https://aura.com"),
]


@router.get("/")
async def root():
    return users_fic_list


# path
@router.get("/{id}")
async def user(id: int):
    return search_user(id)


# query
@router.get("/")
async def user(id: int):
    return search_user(id)


# query
@router.get("/userquery/")
async def userq(id: int, name: Optional[str] = None):
    return search_user_query(id, name)


# POST
@router.post("/", status_code=201)
async def user(newuser: User):
    return insert_user(newuser)


# PUT
@router.put("/")
async def user(user: User):
    return change_user(user)

# DELETE
@router.delete("/{id}")
async def user(id: int):
    return delete_user(id)

def search_user_query(id: int, name: str):
    users = filter(
        lambda user2: user2.id == id or (name is not None and user2.name == name),
        users_fic_list,
    )
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}


def search_user(id: int):
    users = filter(lambda user2: user2.id == id, users_fic_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}


def insert_user(new_user: User):
    # Si el resultado de search_user es una instancia de la clase User, significa que el usuario ya existe.
    if type(search_user(new_user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    else:
        users_fic_list.append(new_user)
        return new_user


def change_user(user: User):
    for index, saved_user in enumerate(users_fic_list):
        if saved_user.id == user.id:
            users_fic_list[index] = user
            return user
    return {"error": "No se ha encontrado el usuario"}



def delete_user(id: int):
    for index, user in enumerate(users_fic_list):
        if user.id == id:
            del users_fic_list[index]
            return True
    return {"error": "No se ha encontrado el usuario"}




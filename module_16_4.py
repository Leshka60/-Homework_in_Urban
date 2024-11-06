from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List, Annotated


app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}', response_model=str)
async def create_user(user: User, username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                example='UrbanUser')], age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> User:
    if len(users) == 0:
        user.id = 1
    else:
        user.id = len(users) + 1
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}', response_model=str)
async def update_user(user_id: int, username: str, age: int) -> User:
   for user in users:
       if user.id == user_id:
           user.username = username
           user.age = age
           return user
   raise HTTPException(status_code=404, detail='User was not found')


@app.delete("/user/{user_id}", response_model=str)
async def delete_user(user_id: int = Path(ge=0)) -> str:
    for i, del_user in enumerate(users):
        if del_user.id == user_id:
            users.pop(i)
            return del_user.id
    raise HTTPException(status_code=404, detail='User was not found')

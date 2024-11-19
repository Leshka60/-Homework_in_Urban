from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import *
from app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify


router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users


@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    sought_user = db.scalar(select(User).where(User.id == user_id))
    if not sought_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return sought_user


@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], new_user: CreateUser):
    append_user = db.scalar(select(User).where(User.username == create_user.username))
    if append_user is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Username already exists')
    db.execute(insert(User).values(username=new_user.username,
                                   firstname=new_user.firstname,
                                   lastname=new_user.lastname,
                                   age=new_user.age,
                                   slug=slugify(new_user.username)))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_user: UpdateUser):
    change_user = db.scalar(select(User).where(User.id == user_id))
    if not change_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    db.execute(update(User).where(User.id == user_id).values(username=update_user.username,
                                                             firstname=update_user.firstname,
                                                             lastname=update_user.lastname,
                                                             age=update_user.age,
                                                             slug=slugify(update_user.username)))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    existing_user = db.scalar(select(User).where(User.id == user_id))
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    db.execute(delete(Task).where(Task.user_id == user_id))
    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User delete is successful!'}


@router.get('/{user_id}/tasks')
async def tasks_by_user_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    tasks = db.scalar(select(Task).where(Task.user_id == user_id)).all()
    return tasks

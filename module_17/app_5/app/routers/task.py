from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import *
from app.schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    sought_task = db.scalars(select(Task).where(Task.id == task_id))
    if not sought_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return sought_task


@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], create_task_: CreateTask, user_id: int):
    found_user = db.scalars(select(User).where(User.id == user_id))
    if not found_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    db.execute(insert(Task).values(title=create_task_.title,
                                   content=create_task_.content,
                                   priority=create_task_.priority,
                                   user_id=user_id,
                                   slug=slugify(create_task_.title)))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, update_task: UpdateTask):
    change_task = db.scalars(select(Task).where(Task.id == task_id))
    if not change_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    db.execute(update(Task).where(Task.id == task_id).values(title=update_task.title,
                                                             content=update_task.content,
                                                             priority=update_task.priority,
                                                             slug=slugify(update_task.title)))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    existing_task = db.scalars(select(Task).where(Task.id == task_id))
    if not existing_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User delete is successful!'}

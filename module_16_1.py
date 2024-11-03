from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def welcome():
    return 'Главная страница'


@app.get('/user/admin')
async def us_admin():
    return f'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def us_id(user_id: str):
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user/{user_name}/{age}')
async def us_inf(user_name: str, age: str):
    return f'Информация о пользователе. Имя: {user_name}, Возраст: {age}'

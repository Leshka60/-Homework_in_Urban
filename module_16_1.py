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


@app.get('/user/{username}/{age}')
async def us_inf(username: str, age: int):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'

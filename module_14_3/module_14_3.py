from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import tracemalloc
tracemalloc.start()


api = "7634455574:AAETXjoYUI9Qka1k-JDs4Tkj4P3TxHjOe08"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


kb = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 =KeyboardButton(text='Купить')
kb.add(button1, button2, button3)


inline_kb_form = InlineKeyboardMarkup(row_width=2)
inline_button_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
inline_button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb_form.add(inline_button_calories, inline_button_formulas)


inline_kb_prod = InlineKeyboardMarkup(row_width=4)
ib_product1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
ib_product2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
ib_product3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
ib_product4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
inline_kb_prod.add(ib_product1, ib_product2, ib_product3, ib_product4)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    with open('Product1.jpg', 'rb') as p1:
        await message.reply_photo(p1, f'Название: Product1 | Описание: описание 1 | Цена: {1 * 100}')
    with open('Product2.jpg', 'rb') as p2:
        await message.reply_photo(p2, f'Название: Product2 | Описание: описание 2 | Цена: {2 * 100}')
    with open('Product3.jpg', 'rb') as p3:
        await message.reply_photo(p3, f'Название: Product3 | Описание: описание 3 | Цена: {3 * 100}')
    with open('Product4.jpg', 'rb') as p4:
        await message.reply_photo(p4, f'Название: Product4 | Описание: описание 4 | Цена: {4 * 100}')
    await message.answer('Выберите продукт для покупки:', reply_markup=inline_kb_prod)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_kb_form)


@dp.callback_query_handler(text='formulas')
async def formulas(call):
    await call.message.answer('Формула Миффлина-Сан Жеора:\n'
                              'Для мужчин: 10 * вес + 6.25 * рост - 5 * возраст + 5\n'
                              'Для женщин: 10 * вес + 6.25 * рост - 5 * возраст - 161')


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer(f'Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer(f'Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    calories_men = 10 * weight + 6.25 * growth - 5 * age + 5
    calories_women = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f'Норма калорий для мужчин - {calories_men} \n'
                         f'Норма калорий для женщин - {calories_women}')

    await state.finish()


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer(f'Привет! Я бот помогающий твоему здоровью. '
                         'Нажми, пожалуйста, кнопку «Рассчитать», чтобы узнать свою норму калорий, '
                         'или кнопку "Купить" для приобретения продукта.',
                         reply_markup=kb)


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

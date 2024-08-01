class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if 1000000 <= vin <= 9999999 and isinstance(vin, int):
            self.__vin = vin
        else:
            raise IncorrectVinNumber(vin)
        if isinstance(numbers, str) and len(numbers) == 6:
            self.__numbers = numbers
        else:
            raise IncorrectCarNumbers(numbers)


class IncorrectVinNumber(Exception):
    def __init__(self, vin):
        self.vin = vin

    def __str__(self):
        if not (1000000 <= self.vin <= 9999999):
            return f'Неверный диапазон для vin номера'
        elif not isinstance(self.vin, int):
            return f'Некорректный тип vin номера'


class IncorrectCarNumbers(Exception):
    def __init__(self, numbers):
        self.numbers = numbers

    def __str__(self):
        if not isinstance(self.numbers, str):
            return f'Некорректный тип данных для номеров'
        elif len(self.numbers) != 6:
            return f'Неверная длина номера'


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.__str__())
except IncorrectCarNumbers as exc:
    print(exc.__str__())
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.__str__())
except IncorrectCarNumbers as exc:
    print(exc.__str__())
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.__str__())
except IncorrectCarNumbers as exc:
    print(exc.__str__())
else:
    print(f'{third.model} успешно создан')

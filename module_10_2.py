from time import sleep
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        warrior = 100
        past_day = 0
        print(f'{self.name}, на нас напали!')
        while warrior > 0:
            warrior -= self.power
            sleep(1)
            past_day += 1
            print(f'{self.name} сражается {past_day} день(дня, дней), осталось {warrior} воинов.')
        print(f'{self.name} одержал победу спустя {past_day} дней!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

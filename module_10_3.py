import threading
from threading import Lock
from time import sleep
import random


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            monies = random.randint(50, 500)
            self.balance += monies
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {monies}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for _ in range(100):
            monies = random.randint(50, 500)
            print(f'Запрос на {monies}')
            if monies <= self.balance:
                self.balance -= monies
                print(f'Снятие: {monies}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

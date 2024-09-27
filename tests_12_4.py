import rt_with_exceptions
import unittest
import logging


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTests(unittest.TestCase):

    def test_walk(self):
        try:
            runner = rt_with_exceptions.Runner(name='Вася', speed=-5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner')

    def test_run(self):
        try:
            runner = rt_with_exceptions.Runner(name=5, speed=10)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner')


if __name__ == '__main__':
    unittest.main()

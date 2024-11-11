# Lambda-функция:
# Даны 2 строки:
# first = 'Мама мыла раму'
# second = 'Рамена мало было'
# Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
# Здесь ? - место написания lambda-функции.
#
# Результатом должен быть список совпадения букв в той же позиции:
# [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
# Где True - совпало, False - не совпало.
import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))


# Замыкание:
# Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
# Внутри этой функции, напишите ещё одну - write_everything(*data_set), где *data_set - параметр принимающий неограниченное количество данных любого типа.
# Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
# Функция get_advanced_writer возвращает функцию write_everything.
#
# Данный код:
# write = get_advanced_writer('example.txt')
# write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

def get_advanced_writer(file_name: str):

    def write_everything(*data_set):

        try:
            with open(file=file_name, mode='w', encoding='UTF-8') as file:

                for text in data_set:
                    file.write(text.__str__() + '\n')

        except Exception as e:

            print(e)

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__:
# Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
# В этом классе также определите метод __call__ который будет случайным образом выбирать слово из words и возвращать его. Для случайного выбора с одинаковой вероятностью для каждого данного в коллекции можете использовать функцию choice из модуля random.
#
# Ваш код (количество слов для случайного выбора может быть другое):
# from random import choice
# # Ваш класс здесь
# first_ball = MysticBall('Да', 'Нет', 'Наверное')
# print(first_ball())
# print(first_ball())
# print(first_ball())

class MysticBall:

    def __init__(self, *words):

        self.words: list[str] = list(words)

    def __call__(self, *args, **kwargs) -> str:

        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball.words)
print(first_ball())
print(first_ball())
print(first_ball())
# Приведем плейлист песен в виде списка списков и словаря.
# Посчитайте общее время звучания трех случайных песен.
# Используйте модули random и datetime. Или любые другие.
# Подумайте, как можно представить решение в виде одной функции, которая принимает разные типы данных?

from pprint import pprint

# список списков
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# словарь - хеш-таблица
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# 4. Создать функцию из готового решения
# импорты
import random
from datetime import timedelta

def time_table(playlist):
  summa=timedelta(minutes=0, seconds=0)  # общее время звучания
  for key in random.sample(playlist.keys(), k=3): # с помощью цикла выбираем ключи песен
      ms = str(playlist[key]) .split('.')
      summa = summa + timedelta(minutes=int(ms [0]), seconds=int(ms [1]))
  return summa

# вызов функции
print(f"Время звучания: {time_table(my_favorite_songs_dict)}") 

# 10.469999999999999



# # пример функции
# def hello(name):
#     return f"Hello {name}"
#     # return "Hello " + namep

# print(hello("Nikita"))
# print(hello("Aleksandr"))
# print(hello("Anastasia"))
# print(hello("Mila"))






# # 3. вывести три случайные песни из словаря

# import random

# ## randint выбирает int из диапазона
# ## uniform выбирает float из диапазона
# print(random.randint(0, 10))
# print(random.uniform(0.2, 7.5))

# ## объявление списка
# primes = list(range(50))
# ## перемешаем список
# random.shuffle(primes)
# print(primes)
# ## выбрать одно значение
# print(random.choice(primes))

# ## выбрать несколько значений
# print(random.choices(primes, k=3)) # возвращает с повторениями
# print(random.sample(primes, k=3)) # без повто


# # TODO - найти время звучания трех случайных песен


# # 2. Найти время звучания трез первых песен из словаря?
# # # Как получить значени из словаря
# print(my_favorite_songs_dict['In This World'])
# # my_favorite_songs_dict["Follow"] = 3.15
# # pprint(my_favorite_songs_dict)

# # print(my_favorite_songs_dict.keys())
# # print(my_favorite_songs_dict.values())

# summa=0  # общее время звучания

# for key in random.sample(my_favorite_songs_dict.keys(), k=3): # с помощью цикла выбираем ключи песен
#     summa = summa + my_favorite_songs_dict[key]
    
# print(summa)






# # # 1. как получить время звучание трех первых песен из списка?
# # # Как получить время звучания песни?
# # print(my_favorite_songs[0])  # ['Waste a Moment', 3.03]
# # print(my_favorite_songs[0][1])

# # # как получить суммарное время звучания трех первых песен?
# # summa=0
# # for x in range(3):
# #     summa=summa+my_favorite_songs_dict[x][1]
# # print(summa) # 10.45



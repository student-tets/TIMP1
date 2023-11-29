<h1>Основы Python. Задача 1</h1> 
<img src="images/py.png" width="200px"/>

## Условие

```Python
# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.
```

## Решение

### Вариант 1
Воспользуемся индексацией строки и выведем первый трек. Сложно считать индексы в ручную.

```Python
print(my_favorite_songs[0:14])
```

### Вариант 2
Попробуем найти для первой песни индекс запятой, которая разделяет песни. Используем методы find и rfind. Тем не менее, найти запятые для первой и последней песней не составит труда, но как быть с песнями в середине строки.

```Python
# Первая песня
print(my_favorite_songs[:my_favorite_songs.find(',')])
# Последняя песня
print(my_favorite_songs[my_favorite_songs.rfind(','):])
```

### Вариант 3
Воспользуемся другим методом строк – split, который позволяет разделить строку по символам и превратить ее в список.

```Python
# разделить строку по запятой
song_list = my_favorite_songs.split(', ')
print(song_list) # ['Waste a Moment', " Staying' Alive", ' A Sorta Fairytale', ' Start Me Up', ' New Salvation']

# тип данных song_list
print(type(song_list)) # <class 'list'>
# длина song_list
print(len(song_list)) # 5

print(song_list[0])  # первая песня
print(song_list[-1]) # последняя песня
print(song_list[1])  # вторая песня 
print(song_list[-2]) # предпоследняя песня
```


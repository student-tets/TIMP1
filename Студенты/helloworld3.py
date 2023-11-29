# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.
#васильев Никита
#маркеева
#кунин
#михайлюк
print(my_favorite_songs[0:my_favorite_songs.find(',')])
print(my_favorite_songs[25:my_favorite_songs.find(',')])
print(my_favorite_songs.split(','))

song_list = my_favorite_songs.split(',')

print(len(song_list))

print(type(my_favorite_songs))
print(type(song_list))

#задание
shop_list = ['Картофель', 'Горошек', 'Рис', 'Хлеб']
fruits = ['Яблоко', 'Апельсин', 'Клубника']
#   b. Добавьте фрукты из списка fruits в конец списка shop_list

print(shop_list.append(fruits))
#append - добавить в конец
#extend



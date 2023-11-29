# Разбор полетов

# Вариант 1
# Проверьте, содержит ли строка одинаковое количество "x" и "o".
# Верните логическое значение True или False
# Строка может быть в любом регистре и содержать любые символы!

# Примеры ввода/вывода:
#   строка "ooxx" => true
#   строка "xooxx" => false
#   строка "ooxXm" => true
#   строка "zpzpzpp" => true # когда нет "x" и "o", должно быть возвращено значение true
#   строка "zzoo" => false

# def decision(string):
#     string = string.lower()
#     number_of_symbols_x = string.count("x")
#     number_of_symbols_o = string.count("o")
#     return number_of_symbols_x == number_of_symbols_o

# print(decision("ooxx"))
# print(decision("xooxx"))
# print(decision("ooxXm"))
# print(decision("zpzpzpp"))
# print(decision("zzoo"))

# Вариант 6
# Напишите скрипт, который принимает цифры от 0 до 9 и возвращает значение прописью.

# Например,
#   при вводе числа 1 получаем 'Один'
#   при вводе числа 3 получаем 'Три'
#   при вводе числа 10000 получаем None

# Использовать условный оператор if-elif-else нельзя!
# def number_word(number):
#     a = ['ноль', 'один', 'два', 'три', 'четыре', 
#        'пять', 'шесть', 'семь', 'восемь', 'девять']

#     if 0 < number < 10:
#         return a[number]
#     else:
#         return None
# b = int(input())
# c = number_word(b)
# print(c) 



# def aboba(num):
#   if num < 0 or num > 9:
#       return None

#   rap = ["Ноль", "Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Семь", "Восемь", "Девять"]

#   return rap[num]

# user_input = int(input("Введите число от 0 до 9: "))
# print(aboba(user_input))


# Вариант 7
# Вы спрашиваете маленькую девочку: "Сколько тебе лет?"
# Она может ответить вам: "Мне x лет", где x - число от 0 до 9.

# Напишите скрипт, который находит цифру в строке (0-9) и вывожит на в виде целого числа.

# Например,
#   строка "Мне 6 лет" –> 6
#   строка "Мама говорит, что мне 3" –> 3
#   строка "Я ниняяю" –> None

# Допущение,
#  в строке всегда должна быть одна цифра!


def find_digit(response):
  for i in response:
    if i.isdigit():
      return int(i)
print(find_digit("Мне 6 лет"))


# Задача с codewars:

# Вариант 1
def neutralise(s1, s2):
    s = ''
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            s += '0'
        else:
            s += s1[i]
    return s

print(neutralise("--++--", "++--++")) # "000000"

# Вариант 2
def neutralise(s1, s2):
    return ''.join('0' if i != j else i for i, j in zip(s1, s2))
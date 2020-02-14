# Task1

# 1 Определите является ли строка записью числа. (Подсказка: ищите как это
# сделать с помощью методов строк)
enter_str = input("Enter a number: ")
is_str_a_number = str.isdigit(enter_str)
print("Is string a number: " + str(is_str_a_number))

# 2. Посчитайте сколько у вас пробелов в строке.
print('It is a good day'.count(' '))

# 3. Посчитайте сколько у вас символов точки "."; в строке.
print('It is a good day. So sunny. So warm.'.count('.'))

# 4. Создайте строку Homework. Преобразуйте её в строку длиной 100 символов,
# посередине которой исходное слово, а с обоих сторон строка заполнена
# пробелами. Выведите её на экран.
st3 = str((' ' * 45) + 'Homework' + (' ' * 46))
print(st3)
print(st3.count(""))

# 5. Сделайте первые буквы слов строки большими (upper case).
st4 = str("my task1 is completed")
print(st4.title())

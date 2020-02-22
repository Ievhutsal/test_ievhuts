# Задание 2
# Пользователь вводит строку. Разрежьте её на две части – равные, если длина строки чётная, а
# если длина строки нечётная, то длина первой части должна быть на один символ больше.
# Переставьте эти две части местами, результат запишите в новую строку и выведите на экран.

enter_sentence = input("Enter string: ")
string_length = len(enter_sentence) + 1
first_part = enter_sentence[: string_length // 2]
second_part = enter_sentence[string_length // 2:]
print(second_part, first_part)


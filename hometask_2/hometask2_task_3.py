# Задание 3
# 1) Напишите счетчик с помощью конструкции while, который выводит числа от 0 до 10.
i = 1
print("Task1  Numbers from 0 - 10")
while i <= 10:
    print(i)
    i += 1

# 2) Напишите счетчик с помощью конструкции while, который выводит числа от 20 до 1.
# Попробуйте вывести числа в одной строчке, разделённые пробелом
x = int(input("Enter a number from 1 till 20: "))
final_string = ""

print("Task2: Numbers from 1 - 20")
while 1 <= x <= 20:
    final_string += str(x) + " "
    x += 1
print(final_string)


# 3) Напишите цикл while, в котором вы, если число чётное, каждую итерацию уменьшаете его
# в 2 раза. Вы делите целое чётное число на 2 пока от него не останется нечётный остаток.
# Посчитайте сколько раз вы делили нацело на 2.
print("Task 3: ")
number = int(input("Input number:"))
counter = 0
while number % 2 == 0:
    number = number // 2
    counter += 1
print(counter)



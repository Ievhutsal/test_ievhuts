# Task 2
# 1. Вычислите длину гипотенузы в прямоугольном треугольнике со сторонами 158 и 971.
a_side = 158 ** 2
b_side = 971 ** 2
hypotenuse = (a_side + b_side) ** 0.5
print("Length of hypotenuse: " + str(hypotenuse))

# 2. Дано двузначное число. Найдите число десятков в нем.
num = 1050
print("Amount of dozens: " + str(int(num // 10)))

# 3. Дано трёхзначное число. Найдите сумму его цифр.
num2 = "786"
count_num2 = int(num2[0]) + int(num2[1]) + int(num2[2])
print("Count sum of numbers: " + str(count_num2))

# 4. Дано целое число n. Выведите следующее за ним чётное число.
next_even = 0
n = int(input("Enter integer number: "))
is_n_even = n % 2 == 0
if is_n_even:
    next_even = n + 2
else:
    next_even = n + 1
print("Next even: " + str(next_even))

# 5. Дано положительное действительное число X. Выведите его дробную часть.
real_num = float(input("Enter any real number: "))
print(real_num % 1)
# 6. Дано положительное действительное число X. Выведите его первую цифру после
# десятичной точки.
real_num_decimal_part = str(real_num % 1)
print("First decimal number : " + str(real_num_decimal_part[2]))

# Задание 3
# Пользователь вводит целое число. Требуется определить, является ли год с данным номером
# високосным. Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что
# в соответствии с григорианским календарём, год является високосным, если его номер кратен 4,
# но не кратен 100, а также если он кратен 400.

year = int(input("Enter number year: "))
is_divided_by_4 = ((year / 4) % 1) == 0
is_divided_by_400 = ((year / 400) % 1) == 0
is_divided_by_100 = ((year / 100) % 1) == 0

if is_divided_by_4:
     if is_divided_by_100:
        if is_divided_by_400:
            print("Yes, it is a leap year")
        else:
            print("No, it is not a leap year")
     else:
        print("Yes, it is a leap year")
else:
    print("No, it is not a leap year")

# Задание 4
# Даны три числа a, b, c. Определите, существует ли треугольник с такими сторонами. Если
# треугольник существует, выведите строку YES, иначе выведите строку NO.

a = float(input('Enter triangle side a: '))
b = float(input('Enter triangle side b: '))
c = float(input('Enter triangle side c: '))

if ((a + b) > c) and ((b + c) > a) and ((a + c) > b):
    print("Yes, it is a triangle")
else:
    print("No, it is not a triangle")

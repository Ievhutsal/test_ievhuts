str_enter = input("enter string:")

if str_enter == "Hi":
    print("Hello")
else:
    print("Bad")
print("Goodbye")

x = 10
while x > 0:
    print(str(x) + '!')
    x -= 1

# f_list = [2, 4, 6, 9, 6, 345]
# while len(f_list) > 0:
#    print(f_list.pop())
# while f_list:
#    print(f_list.pop())

# f_num = int(input("enter full number: "))
# while f_num / 2:
our_list = [1,10, 3, 5, 6, 11]
even = []
odd = []

for item in our_list:
    if item % 2 == 0:
        even.append(item)
    elif item % 2 == 1:
        odd.append(item)
    else:
        print(item, 'is not integer number')


my_list = [1, 10, 3, 5, 6, 11]
y = []
for y in my_list:
    if y % 2 == 0:
        print(y)
    elif y % 2 == 1:
        print(y + 1)

u_list = [1, 10, 3, 5, 6, 11]
for i in range(len(u_list)):
    if u_list[i] % 2 == 1:
        u_list[i] += 1
print(u_list)

l_l = [11, 1, 13]

for i in range(len(l_l)):
    if l_l[i] % 2 != 0:
        l_l[i] += 1
    print(l_l)

while True:
    word = input("Please enter a word: ")
    if ' ' not in word:
        break
#word

while True:
    word_1 = input("Please enter a number: ")
    if word_1.isdigit():
        break
int(word_1)


val = input("Enter value: ")
try:
    val = int(val)
    print(val)
except:
    print("Error!")

s, i = 's', 0
try:
    s = int(s) / i
except ValueError as e:
    print(e)
except ZeroDivisionError:
    print("Zero division error")

print("Goodbye")


def my_fun(times):
    while True:
        c = input("Number")
        try:
          c = float(c)
        except ValueError as e:
          print("enter a number!!!")
        else:
            break
    return c*times

m = my_fun(2)
print(m)


while True:
    number = input("Enter number")
    try:
        number = float(number)
    except ValueError:
        pass
    else:
        break


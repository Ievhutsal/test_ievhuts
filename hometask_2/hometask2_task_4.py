# Задание 4
# У вас есть список чисел.
#1. Напишите цикл, который выводит на экран и удаляет с начала элементы списка, пока он не
# останется пустым
my_list = [1, 3, 6, 33, 221, 56, 66]
while len(my_list) > 0:
    print(my_list.pop(0))

# 2. ** Как сделать это же задание со строкой: напишите цикл, который выводит на экран и
# «удаляет» первый символ строки, пока она не станет пустой?

my_sentence = input("Enter a sentence: ")
while len(my_sentence) > 0:
    print(my_sentence[0])
    my_sentence = my_sentence[1::]
print(my_sentence)

# 3. Напишите цикл, который выводит на экран и удаляет элементы списка от самого
# маленького до самого большого, пока он не останется пустым.
m_list = [1, 3, 6, 33, 221, 56, 66]
while len(m_list) > 0:
    smallest_value = m_list[0]
    smallest_value_index = 0
    for item in m_list:
        if item < smallest_value:
            smallest_value = item
            smallest_value_index = m_list.index(item)
    print(smallest_value)
    m_list.pop(smallest_value_index)


# 4. ** Дана последовательность натуральных ненулевых чисел, завершающаяся числом 0.
# Определите, какое наибольшее число подряд идущих элементов этой последовательности
# равны друг другу.

list_with_numbers = [2, 3, 5, 5, 5, 6, 2, 3, 3, 3, 3, 3, 89, 0]
starting_subsequence_value = list_with_numbers[0]
starting_subsequence_index = 0
end_subsequence_value = list_with_numbers[0]
end_subsequence_index = 0

for current_index in range(len(list_with_numbers) - 1):
    next_number = list_with_numbers[current_index + 1]
    current_number = list_with_numbers[current_index]
    previous_number = list_with_numbers[current_number -1]

    # identify if  starting point
    if previous_number != current_number and current_number == next_number:
        starting_subsequence_value = current_number
        starting_subsequence_index = current_index

    #  identify if  END point
    if previous_number == current_number and current_number != next_number:
        end_subsequence_value = current_number
        end_subsequence_index = current_index






# Задачи на циклы и опаретор условия

''''
Задача 1

Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.

'''
# for i in range(10, 51, 10):
#     print(i)



''''
Задача 2

Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.

'''

# y = 0
# for i in range(1, 11):
#     print('ВВедите число')
#     x = int(input())
#     if x == 5:
#         y += 1
#
# print(y, 'раз ввели число 5!')


''''
Задача 3

Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.

'''
# sum = 0
# for i in range(1, 101):
#     sum += i
# print(sum)


''''
Задача 4

Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.

'''

# y = int(1)
# for i in range(1, 11):
#     y = i*y
# print(y)


''''
Задача 5

Вывести цифры числа на каждой строчке.

'''

# int_numb = 2129
# print(int_numb % 10, int_numb // 10)
#
# while int_numb > 0:
#     print(int_numb % 10)
#     int_numb = int_numb // 10


''''
Задача 6

Найти сумму цифр числа.

'''

# y = 0
# x = 12345
# while x > 0:
#     y = (x % 10)+y
#     x = (x // 10)
#     continue
# print(y)


# У меня вопрос. Как мне написать, что бы работал следующтй код(ниже)?
# y = 0
# x = int(input('Введите число')
# while x > 0:
#     y = (x % 10)+y
#     x = (x // 10)
#     continue
#
# print(y)


''''
Задача 7

Найти произведение цифр числа.

'''

# x = 12345
# y = 1
# while x > 0:
#     y = (x % 10)*y
#     x = x // 10
#     continue
# print(y)


''''
Задача 8

Дать ответ на вопрос: есть ли среди цифр числа 5?

'''

# int_numb = 2536984123032147896932141
# while int_numb > 0:
#     if int_numb % 10 == 5:
#         print('Yes')
#         break
#     int_numb = int_numb // 10
# else:
#     print('No')


''''
Задача 9

Найти максимальную цифру в числе

'''

# x = int(input('Введите ваше число'))
# y = 0
# z = 0
# while x > 0:
#     y = x % 10
#     x = x // 10
#     if y > z:
#         z = y
# print('Максимальная цифра в этом числе:', z)


''''
Задача 10

Найти количество цифр 5 в числе

'''
# x = int(15453201)
# y = 0
# z = 0
# while x > 0:
#     y = (x % 10)
#     x = x // 10
#     if y == 5:
#         z += 1
#
#print('В веденном числе', z, 'пятерок')


# Почему, у меня не идет следующий код?
# x = int(input('Введите число')
# y = 0
# z = 0
# while x > 0:
#     y=(x % 10)
#     x = x // 10
#     if y == 5:
#         z += 1
#
# print('В веденном числе', z, 'пятерок')


'''
Доброго времени суток, на всякий случай, я все закоментил.
Если так делать не нужно, пожалуйста напишите.
Я бы хотел 10 баллов, у меня получается?

'''

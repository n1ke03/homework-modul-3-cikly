# num1 = int(input("Введите целое число: "))
# num2 = int(input("Введите целое число: "))
# for i in range(num1, num2):
#   if i % 7 == 0:
#     print(i)

# for i in range(num1, num2):
#   print(i)
# for i in range(num1, num2, -1):
#   print(i)
# for i in range(num1, num2):
#   if i % 7 == 0:
#     print(i)
# count = 0
# for i in range(num1, num2):
#   if i % 5 == 0:
#     count += 1
#     print(count)

# for i in range(num1, num2):
#   if i % 3 == 0 and i % 5 == 0:
#     print("Fizz Buzz")
#   elif i % 5 == 0:
#     print("Buzz")
#   elif i % 3 == 0:
#     print("Fizz")
#   elif i % 3 and i % 5:
#     print(i)



# num1 = int(input("Введите целое число: "))
# num2 = int(input("Введите целое число: "))
# chet = 0
# nechet = 0
# krat = 0
# a_chet = 0
# a_nechet = 0
# a_krat = 0
# for i in range (num1, num2):
#   if i % 2 ==0:
#     chet += i
#     a_chet = chet / i
#     print(chet, a_chet)
#   elif i %3 ==0:
#     nechet += i
#     a_nechet = nechet / i
#     print(nechet, a_nechet)
#   elif i % 9 ==0:
#     krat += i
#     a_krat = krat / i
#     print(krat, a_krat)

# line = int(input("Введите длину: "))
# symvol = input('Введите символ: ')
# for i in range(line):
#   print(symvol)


# while True:
#   num = int(input("Введите число: "))
#   if num==7:
#     print('Good Bye!')
#     break
#   if num > 0:
#     print('Number is positive')
#   elif num <0:
#     print ('Number is negative')
#   elif num == 0:
#     print ('Number is equal to zero')

# sum = 0
# min = None
# max = None
# while True:
#   num = int(input("Введите число: "))
#   if num==7:
#     print('Good bye')
#     break
#   if min==None and max==None:
#     min = num
#     max = num
#   if num>max:
#     max = num
#   if num<min:
#     min = num
#     sum+=num
#     print(f"min = {min}\nmax = {max}\nsum = {sum}")



# x = int(input('Введите целое число: '))
# y = int(input('Введите целое число возведения в степень: '))
# print(x**y)

# count = 0 
# for i in range(100, 1000): 
#     num = str(i) 
#     if num[0] == num[1] or num[0] == num[2] or num[1] == num[2]: 
#         count += 1 
# print(count)

# count = 0 
# for i in range(100, 10000): 
#     num = str(i) 
#     if num[0] != num[1] or num[0] != num[2] or num[1] != num[2]: 
#         count += 1 
# print(count)

# n = int(input('Введите число: '))
# tail = ''
# while n:
#   if not (n%10==3 or n%10==6):
#     tail = str(n%10) + tail
#   n//=10
# print(tail)

# for i in range(1, 10+1):
#   for j in range(1, 10+1):
#     print(f'{i} * {j} = {i*j}',end='   ')
#   print()

# x = int(input('Введите первое число: '))
# y= int(input('Введите второе число: '))
# for i in range(1, 10+1):
#   print(f'{x} * {i} = {x*i}',end='   ')
# for i in range(1, 10+1):
#   print(f'{y} * {i} = {y*i}', end='   ')
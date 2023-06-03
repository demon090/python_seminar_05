# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

a = int(input('Введите число:   '))
print(' ')
b = int(input('Введите степень:   '))
print(' ')

def degree(a, b):
    if b == 0:
        return 1
    if b < 0:
        return 1 / degree(a, -b)
    return a * degree(a, b - 1)

print(degree(a, b))


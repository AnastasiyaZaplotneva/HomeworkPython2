# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input("введите число "))
x = 1
for y in range(n):
    y = y + 1
    x = y * x
    print(x, end=" ")
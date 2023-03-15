import math

def factorial(n):
    if(n == 1): 
        return 1
    else:
        return (n * factorial(n-1))

def tichChan(n):
    rs = 1
    for i in range(1, n + 1) :
        print(i)
        rs = rs * i
    return rs

def tichLe(n):
    rs = 1
    for i in range(1, n + 1) :
        print(i)
        rs = rs * i
    return rs

print("Nhập x: ")
x = float(input())
print("Nhập eps: ")
eps = float(input())

mu = 1
first = x
second = first + x**mu/factorial(mu+2)
while(math.fabs(first - second) > eps):
    mu += 2 
    first = second
    second = first + x**mu/factorial(mu+2)
print(first)
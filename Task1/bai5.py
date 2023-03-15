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
first = 1
dau = -1
second = first + dau *tichLe(mu*2)/ tichChan(mu * 2) * x**mu
while (math.fabs(first-second)>eps):
    mu = mu + 1
    dau = -dau 
    first = second
    second = first + dau* tichLe(mu*2)/ tichChan(mu * 2) * x**mu
print(first)
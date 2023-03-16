import random

#1.	Viết hàm sinh ngẫu nhiên dữ liệu cho tập tin input.txt có cấu trúc sau:
def randomRect():
    f = open("input.txt", "a")
    for i in range(5):
        d = random.randint(10, 100)
        r = random.randint(10, 100)
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        f.write(f"{d} {r} {x} {y}\n")
    f.close()


def randomCircle():
    f = open("input.txt", "a")
    for i in range(5):
        r = random.randint(10, 100)
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        f.write(f"{r} {x} {y}\n")
    f.close()


def randomTriangle():
    f = open("input.txt", "a")
    for i in range(5):
        a = random.randint(10, 100)
        b = random.randint(10, 100)
        c = random.randint(10, 100)
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        if (a + b > c or a + c > b or b + c > a) and (a - b < c or a - c < b or b - c < a):
            f.write(f"{a} {b} {c} {x} {y}\n")
    f.close()

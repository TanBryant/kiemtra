import math


class Shape:
    def __int__(self, x, y):
        self.x = x
        self.y = y

    def chuVi(self):
        pass

    def dienTich(self):
        pass


class Circle(Shape):

    def __int__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

    def chuVi(self):
        return 2 * math.pi * float(self.r)

    def dienTich(self):
        return math.pow(float(self.r), 2)

    def printItem(self):
        return f"Bán kính {self.r} có tọa độ ({self.x},{self.y})"


class Rect(Shape):

    def __int__(self, a, b, x, y):
        self.a = a
        self.b = b
        self.x = x
        self.y = y

    def chuVi(self):
        return (float(self.a) + float(self.b)) * 2

    def dienTich(self):
        return float(self.a) * float(self.b)

    def printItem(self):
        return f"Chiều dài {self.a} và chiều rộng {self.b} có tọa độ ({self.x},{self.y})"


class Triangle(Shape):

    def __int__(self, a, b, c, x, y):
        self.a = a
        self.b = b
        self.c = c
        self.x = x
        self.y = y

    def chuVi(self):
        return float(self.a) + float(self.b) + float(self.c)

    def dienTich(self):
        p = self.chuVi() / 2
        result = abs(p * (p - float(self.a)) * (p - float(self.b)) * (p - float(self.c)))
        return math.sqrt(result)

    def printItem(self):
        return f"Cạnh a: {self.a}, cạnh b: {self.b}, cạnh c: {self.c} có tọa độ ({self.x},{self.y})"

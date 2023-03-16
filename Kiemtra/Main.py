from Models import Rect, Circle, Triangle
from Random import randomCircle, randomRect, randomTriangle


# a)	Đọc dữ liệu các hình từ tập tin input.txt
def readData():
    list = []
    file = open('input.txt', 'r')
    for line in file.readlines():
        splitText = line.split(" ")
        if len(splitText) == 4:
            rect = Rect()
            rect.a = splitText[0]
            rect.b = splitText[1]
            rect.x = splitText[2]
            rect.y = splitText[3].replace("\n", "")
            list.append(rect)
        elif len(splitText) == 3:
            circle = Circle()
            circle.r = splitText[0]
            circle.x = splitText[1]
            circle.y = splitText[2].replace("\n", "")
            list.append(circle)
        else:
            triangle = Triangle()
            triangle.a = splitText[0]
            triangle.b = splitText[1]
            triangle.c = splitText[2]
            triangle.x = splitText[3]
            triangle.y = splitText[4].replace("\n", "")
            list.append(triangle)
    file.close()
    return list

# b)	Liệt kê hình có chu vi lớn nhât, diện tích lớn nhất 
if __name__ == '__main__':
    #hàm sinh ngẫu nhiên dữ liệu
    randomRect()
    randomCircle()
    randomTriangle()

    # Đọc dữ liệu từ file
    list = readData()

    # Tìm chu vi và diện tích lớn nhất
    ChuviMax = list[0]
    DienTichMax = list[0]

    for item in list:
        if item.chuVi() > ChuviMax.chuVi():
            ChuviMax = item
        if item.dienTich() > DienTichMax.dienTich():
            DienTichMax = item

    print(f"Hình có chu vi lớn nhất: {ChuviMax.printItem()}")
    print(f"Hình có diện tích lớn nhất: {DienTichMax.printItem()}")

import mysql.connector, openpyxl

myconn = mysql.connector.connect(host = "localhost", user = "root",
passwd = "", database = "python")
cur = myconn.cursor()
sql = ("insert into sinhvien(MaSV, Ho, Ten, NgaySinh, Toan, Ly, Hoa) "
+ "values (%s, %s, %s, %s, %s, %s, %s)")
val = ("sv01", "Nguyen Nhat","Tan","02-05-2001", 9, 1.6,6.4)

wb = openpyxl.load_workbook("input.xlsx")
# print(wb.sheetnames)
ws = wb[wb.sheetnames[0]]
for i in range(12, 63): 
    # print(ws.cell(row=i, column=2).value)
    val = (ws.cell(row=i, column=2).value, ws.cell(row=i, column=3).value, ws.cell(row=i, column=4).value, ws.cell(row=i, column=5).value, ws.cell(row=i, column=6).value, ws.cell(row=i, column=7).value, ws.cell(row=i, column=8).value)
    try:
        cur.execute(sql,val)
        myconn.commit()
    except:
        myconn.rollback()
# print(cur.rowcount,"record inserted!")
myconn.close()





# myconn = mysql.connector.connect(host = "localhost", user = "root",
# passwd = "", database = "python")
# cur = myconn.cursor()

# try:
#     cur.execute("update sv set hoten = 'Tân' where id = 'C200111'")
#     myconn.commit()

# except:
#     myconn.rollback()
#     myconn.close()



# import mysql.connector
# #tạo đối tượng connection
# myconn = mysql.connector.connect(host = "localhost", user = "root",
# passwd = "", database = "python")
# #tạo đối tượng cursor
# cur = myconn.cursor()
# try:
# # cập nhật name cho bảng Employee
#     cur.execute("DELETE FROM sv WHERE 1")
#     myconn.commit()
# except:
#     myconn.rollback()
    # myconn.close()

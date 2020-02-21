import csv

import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='assessment4')
cursor = mydb.cursor()

f = open("product.csv", "r")
data = csv.reader(f)
for i in data:
    print(i)
    cursor.execute("insert into product(id, product_name, product_code, price) values(%s, %s, %s , %s)", i)

f1 = open("sale.csv", "r")
data = csv.reader(f1)
for i in data:
    print(i)
    cursor.execute("insert into sale(id, bill_date, product_id, product_quantity) values(%s, %s, %s , %s)", i)


# cursor.execute("select * from product")
# cursor.execute("select * from sale")
#
# r = cursor.fetchall()
# for i in r:
#     print(i)
mydb.commit()

mydb.close()

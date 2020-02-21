import mysql.connector
import logging

mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='assessment4')

logging.basicConfig(filename="logfile.txt",
                    filemode='a',
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger()
logger.info("Database connection established successful with server address and host")
cursor = mydb.cursor()


class Query:
    def query1():
        print('This is query 1')
        cursor.execute(
            "select p.id, p.product_name, p.product_code, p.price, s.bill_date, s.product_quantity from product p "
            "join sale s on p.id = s.product_id having s.product_quantity = (select max(product_quantity) from sale)")
        r = cursor.fetchall()
        for i in r:
            print(i)
        print()
        mydb.commit()
        logger.info("Printing maximum - sold product with product details executed successfully")

    def query2():
        print('This is query 2')
        cursor.execute(
            "select p.id, p.product_name, p.product_code, p.price, s.bill_date, s.product_quantity from product p "
            "join sale s on p.id = s.product_id having s.product_quantity = (select min(product_quantity) from sale)")
        r = cursor.fetchall()
        for i in r:
            print(i)
        print()
        mydb.commit()
        logger.info("Printing minimum - sold product with product details executed successfully")

    def query3():
        print('This is query 3')
        date1 = input('Enter date: ')
        logger.info("user input date taken")
        cursor.execute(
            "select p.id, p.product_name, p.product_code, (p.price*s.product_quantity) as total_amount, s.bill_date, "
            "s.product_quantity from product p "
            "join sale s on p.id = s.product_id where s.bill_date = %s", (date1,))
        r = cursor.fetchall()
        for i in r:
            print(i)
        print()
        mydb.commit()
        logger.info("Getting the billing date from user and print the product details and total amount of displaying "
                    "products executed successfully")

    def query4():
        print('This is query 4')
        p_code = input('Enter the product code: ')
        logger.info("user input product code taken")
        cursor.execute("select id, product_name, price from product where product_code = %s", (p_code,))
        r = cursor.fetchall()
        for i in r:
            print(i)
        print()
        mydb.commit()
        logger.info("Getting the product code from user and check it in product table executed successfully")

    def query5():
        print('This is query 5')
        prod_id = input('Enter product id: ')
        prod_name = input('Enter product name: ')
        prod_code = input('Enter product code: ')
        amount = input('Enter product price: ')
        cursor.execute("insert into product values(%s, %s, %s, %s)", (prod_id, prod_name, prod_code, amount))
        cursor.execute("select * from product")
        r = cursor.fetchall()
        for i in r:
            print(i)
        print()
        mydb.commit()
        logger.info("Adding some products to product table executed successfully")


q = Query
q.query1()
q.query2()
q.query3()
q.query4()
q.query5()

mydb.close()

import mysql.connector


class SwipeTime:
    def __init__(self):
        db = mysql.connector.connect(host='localhost', user='root', passwd='root', database='demo')
        self.db = db
        self.cursor = db.cursor()

    def average_time(self):
        try:
            year = int(input("Enter year:"))
            sql = "select id, month(swipe_date) as month, avg_time from (select id, swipe_date, round(avg(time_out-time_in) " \
                  "over(partition by month(swipe_date) order by month(swipe_date)),4)avg_time from swipe " \
                  "where year(swipe_date) = '{}')t group by month(swipe_date)".format(year)
            self.cursor.execute(sql)
			
            r = self.cursor.fetchall()
            for i in r:
                print(i)


        except Exception as e:
            print(e)

        finally:
            self.db.close()


if __name__ == "__main__":
    obj = SwipeTime()
    obj.average_time()

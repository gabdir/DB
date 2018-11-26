import datetime
import math

import psycopg2

class DB():

    def __init__(self):
        """ create tables in the PostgreSQL database"""
        commands = (
            """
            CREATE TABLE Company (
                Company_id SERIAL PRIMARY KEY,
                Company_name VARCHAR(255) NOT NULL
            )
            """,
            """ 
            CREATE TABLE Station (
                UID SERIAL PRIMARY KEY,
                Location POINT NOT NULL,
                Price_of_charging INTEGER NOT NULL,
                Plug_formats VARCHAR(255) NOT NULL,
                Free_sockets INTEGER NOT NULL,
                Amount_of_sockets INTEGER NOT NULL,
                company_id SERIAL NOT NULL,
                FOREIGN KEY (company_id) REFERENCES Company(company_id) ON UPDATE CASCADE ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE Workshops (
                WID SERIAL PRIMARY KEY,
                Location POINT NOT NULL,
                Available_car_p VARCHAR(255) NOT NULL,
                Available_time VARCHAR(255) NOT NULL,
                company_id SERIAL NOT NULL,
                FOREIGN KEY (company_id) REFERENCES Company(company_id) ON UPDATE CASCADE ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE Provider (
                PCompany_id SERIAL PRIMARY KEY,
                Phone_num VARCHAR(10) NOT NULL,
                Address VARCHAR(255) NOT NULL,
                Name VARCHAR(30) NOT NULL
            )
            """,
            """
            CREATE TABLE Customer (
                Username SERIAL PRIMARY KEY,
                Email VARCHAR(20) NOT NULL,
                Phone_number VARCHAR(10) NOT NULL,
                Location POINT NOT NULL,
                Full_name VARCHAR(30) NOT NULL
            )
    
            """,
            """
            CREATE TABLE Car (
                Identification_num SERIAL PRIMARY KEY,
                Model VARCHAR(255) NOT NULL,
                Status VARCHAR(255) NOT NULL,
                Location POINT NOT NULL,
                Plate VARCHAR(10),
                company_id SERIAL NOT NULL,
                Color VARCHAR(10) NOT NULL,
                FOREIGN KEY (company_id) REFERENCES Company(company_id) ON UPDATE CASCADE ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE History_of_providing (
                providing_id SERIAL PRIMARY KEY,
                WID SERIAL,
                PCompany_id SERIAL,
                Type_car_p VARCHAR(40), 
                FOREIGN KEY (PCompany_id) REFERENCES Provider(pcompany_id) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (WID) REFERENCES Workshops(wid) ON UPDATE CASCADE ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE History_of_charging (
                charging_id SERIAL PRIMARY KEY,
                Identification_num SERIAL,
                UID SERIAL,
                starting_ch TIME,
                ending_ch TIME,
                date DATE,
                FOREIGN KEY (Identification_num) REFERENCES Car(identification_num) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (UID) REFERENCES Station(uid) ON UPDATE CASCADE ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE History_of_trip (
                trip_id SERIAL PRIMARY KEY,
                Identification_num SERIAL,
                Username SERIAL,
                starting_loc POINT,
                client_loc POINT,
                final_loc POINT,
                date DATE,
                starting_tr TIME,
                ending_tr TIME,
                price DOUBLE PRECISION,
                location VARCHAR(255),
                FOREIGN KEY (Identification_num) REFERENCES Car(identification_num) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (Username) REFERENCES Customer(username) ON UPDATE CASCADE ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE History_of_repairing(
                repairing_id SERIAL PRIMARY KEY,
                Identification_num SERIAL,
                WID SERIAL,
                price DOUBLE PRECISION,
                Car_parts VARCHAR(40),
                date DATE,
                FOREIGN KEY (Identification_num) REFERENCES Car(identification_num) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (WID) REFERENCES Workshops(wid) ON UPDATE CASCADE ON DELETE CASCADE
            )
            """

        )
        try:
            self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
            cur = self.conn.cursor()

            '''''for command in commands2:
                cur.execute(command)'''''
            for command in commands:
                cur.execute(command)

            cur.close()

            self.conn.commit()

        except (Exception, psycopg2.DatabaseError) as err:
            print(err)
            pass
        finally:
            self.conn.close()

    def delete_tables(self):

        command = """
        DROP TABLE 
        Company, 
        Station,
        Workshops, 
        Provider,
        Car, 
        Customer, 
        History_of_providing, 
        History_of_charging,
        History_of_trip, 
        History_of_repairing   CASCADE 
        """

        try:
            self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")

            cur = self.conn.cursor()

            '''''for command in commands2:
                cur.execute(command)'''''
            cur.execute(command)

            cur.close()

            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            pass

        finally:
            self.conn.close()

    def input_sample_data(self):
        commands = (""" INSERT INTO company (company_name) VALUES ('Aidar') """,
                    """
                    INSERT INTO station (location, price_of_charging, plug_formats, free_sockets, amount_of_sockets, company_id)
                    VALUES ('(25,25)', '100', 'all', '7', '7', '1'),
                        ('(25,75)', '200', 'all', '7', '7', '1'),
                        ('(75,25)', '100', 'all', '7', '7', '1'),
                        ('(75,75)', '200', 'all', '7', '7', '1')
                    """,
                    """
                    INSERT INTO workshops (location, available_car_p, available_time, company_id)
                    VALUES
                        ('(26,26)', 'some1', '8-20', '1'),
                        ('(26,76)', 'some2', '6-20', '1'),
                        ('(76,26)', 'some3', '4-20', '1'),
                        ('(76,76)', 'some4', '3-20', '1')
                    """,
                    """
                    INSERT INTO provider (phone_num, address, name)
                    VALUES ('977722677', 'Kazan', 'YaSuperProvider'),
                        ('977722591', 'Elabuga', 'TopProvider'),
                        ('917228678', 'Chelny', 'Super777'),
                        ('965228888', 'Yekab', 'Prov21'),
                        ('917228666', 'Ilnov', 'Provider01')
                    """,
                    """
                    INSERT INTO customer (email, phone_number, location, full_name)
                    VALUES('larisa@mail.ru', '8777345621', '(231,129)', 'Cool Per'),
                    ('vitalii2@mail.ru', '8777345623', '(179,35)', 'Vitalii Pol'),
                    ('zakir@mail.ru', '8917914623', '(130,61)', 'Zakir Nur'),
                    ('artur@mail.ru', '8977201655', '(201,54)', 'Artur Akh'),
                    ('ilnur@mail.ru', '8777666623', '(801,555)', 'Ilnur Tel')
                    """,
                    """
                    INSERT INTO car (model, status, location, plate, color, company_id)
                    VALUES ('CH11', 'used', '(123,43)', 'AN10200CS', 'red', '1'),
                        ('CH12', 'used', '(56,74)', 'AN10200CS', 'red', '1'),
                        ('Toyota', 'unused', '(197,31)', 'AF2001', 'blue', '1'),
                        ('Nissan', 'unused', '(65,87)', 'AC901', 'black', '1'),
                        ('Rav4', 'unused', '(77,87)', 'AK901', 'orange', '1')
                    """,

                    """
                    INSERT INTO history_of_providing (wid, pcompany_id, type_car_p)
                    VALUES ('2', '1', 'dich1'),
                        ('3', '2', 'dich2')
                    """,
                    """
                    INSERT INTO history_of_charging (identification_num, uid, starting_ch, ending_ch, date)
                    VALUES ('1', '2', '8:00', '8:50', '2018-11-25'),
                     ('2', '3', '10:00', '10:10', '2018-11-26'),
                     ('3', '3', '11:00', '11:30', '2018-11-24')
                    """,
                    """
                    INSERT INTO history_of_trip (identification_num, username, starting_loc, client_loc, final_loc,date,starting_tr,ending_tr, price, location)
                    VALUES 
                    ('1', '1', '(3,10)', '(7, 13)', '(2, 4)','2018.11.24','2018.11.24 9:00','2018.11.24 10:00', '200', 'Kazan'),
                    ('2', '2', '(1, 5)', '(3, 8)', '(8, 9)','2018.11.26','2018.11.26 17:00','2018.11.26 19:00', '300', 'Kazan'),
                    ('1', '2', '(6, 3)', '(5, 5)', '(10, 6)','2018.11.26','2018.11.26 15:00','2018.11.26 16:00', '500', 'Chelny')
                    """,
                    """
                    INSERT INTO history_of_repairing (identification_num, wid, price, car_parts, date)
                    VALUES ('1', '2', 500, 'dich1', '2018.11.11')
                    """)

        try:
            self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")

            cur = self.conn.cursor()

            for command in commands:
                cur.execute(command)

            cur.close()

            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            pass

        finally:
            self.conn.close()

    # class select_queries():
    def query_1(self, username):
        query = """SELECT * FROM Car NATURAL JOIN history_of_trip WHERE color='red' AND plate LIKE 'AN%' AND 
                  username=""" + str(username) + """ AND 
                  date = CURRENT_DATE
            """
        try:
            self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
            cur = self.conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()

            for row in rows:
                print(row[0])

            cur.close()
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            self.conn.close()

    def query_2(self, date):
        time = datetime.datetime.strptime(date, "%Y-%m-%d")
        time2 = datetime.datetime.strptime(date, "%Y-%m-%d") + datetime.timedelta(hours=1)
        for i in range(24):
            query = """SELECT COUNT(identification_num)
                      FROM history_of_charging
                      WHERE date = '""" + date + """' and starting_ch < '""" + str(time2).split(" ")[
                1] + """' and ending_ch > '""" + str(time).split(" ")[1] + """'"""

            time = time + datetime.timedelta(hours=1)
            time2 = time2 + datetime.timedelta(hours=1)
            try:
                self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
                cur = self.conn.cursor()
                cur.execute(query)
                count = cur.fetchall()[0][0]
                print(count)

                cur.close()
                self.conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)

            finally:
                self.conn.close()
        #

    def query_3(self, date):
        time = datetime.datetime.strptime(date, "%Y-%m-%d")
        self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
        cur = self.conn.cursor()
        time_arr = [[7, 10], [12, 14], [17, 19]]
        cur.execute("""SELECT COUNT(identification_num) FROM Car""")
        car_amount = cur.fetchall()[0][0]
        average_amount = [[], [], []]
        k = 0
        for i in range(7):
            for j in time_arr:
                query = """SELECT COUNT(identification_num)
                    FROM history_of_trip
                    WHERE date = '""" + str(time).split(" ")[0] + """' and starting_tr<'""" + str(j[1]) + """:00:00' and
                    ending_tr>'""" + str(j[0]) + """:00:00'"""
                time = time + datetime.timedelta(days=1)
                cur.execute(query)
                average_amount[k].append(cur.fetchall()[0][0] / car_amount)
                k += 1

            k = 0

        morning = sum(average_amount[0]) / 7
        afternoon = sum(average_amount[1]) / 7
        evening = sum(average_amount[2]) / 7

        print(morning, afternoon, evening)
        self.conn.close()

    def query_4(self, username):
        date = datetime.datetime.now() - datetime.timedelta(days=30)
        self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
        cur = self.conn.cursor()

        cur.execute("""select * from history_of_trip first
        where date > '""" + str(date).split(" ")[0] + """'
        and (select count(*) from history_of_trip second
        where first.starting_tr = second.starting_tr 
        and first.ending_tr = second.ending_tr 
        and first.username = second.username 
        and first.identification_num = second.identification_num 
        and first.date = second.date 
        and first.price = second.price) > 1""")

        try:
            print(cur.fetchall()[0][0] > 0)
        except(IndexError):
            print(False)
            pass

        self.conn.close()

    def query_5(self, date):
        date_cur = datetime.datetime.strptime(date, "%Y-%m-%d")
        self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
        cur = self.conn.cursor()

        cur.execute("""SELECT COUNT(identification_num) FROM Car""")
        car_amount = cur.fetchall()[0][0]

        query1 = """SELECT starting_loc <-> client_loc FROM history_of_trip WHERE date='""" + str(date_cur) + """'"""

        cur.execute(query1)
        list1 = cur.fetchall()

        distance = []
        for i in range(len(list1)):
            distance.append(list1[i][0])
        # average_distance
        print(sum(distance) / len(list1))

        query2 = """SELECT ending_tr-starting_tr FROM history_of_trip WHERE date='""" + str(date_cur) + """'"""
        cur.execute(query2)
        list2 = cur.fetchall()

        time = []
        summ = datetime.timedelta(0)
        for i in range(len(list1)):
            time.append(list2[i][0])
            summ += time[-1]

        summ = summ / len(time)
        # average_time
        print(summ)
        # average_time
        self.conn.close()

    def query_6(self, date):
        time = datetime.datetime.strptime(date, "%Y-%m-%d")
        self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
        cur = self.conn.cursor()
        time_arr = [[7, 10], [12, 14], [17, 19]]
        average_amount = [[], [], []]
        k = 0
        for j in time_arr:
            query = """SELECT COUNT(location), location
            FROM history_of_trip
            WHERE date = '""" + str(time).split(" ")[0] + """' and starting_tr<'""" + str(j[1]) + """:00:00' and
            ending_tr>'""" + str(j[0]) + """:00:00' GROUP BY location"""
            cur.execute(query)
            arr = cur.fetchall()
            try:
                average_amount[k].append([arr[0][0], arr[0][1]])
            except(IndexError):
                pass
            k += 1

        for i in average_amount:
            i.sort()
            try:
                print(i[0][1])
            except(IndexError):
                print(None)

        self.conn.close()

    def query_7(self, date):
        print("\nQuery 7:")
        time = datetime.datetime.strptime(date, "%Y-%m-%d") - datetime.timedelta(days=90)
        self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
        cur = self.conn.cursor()
        cur.execute("""SELECT identification_num FROM Car""")
        id = cur.fetchall()
        date2 = str(time).split(" ")[0]
        arr = []
        for i in id:
            query = """SELECT COUNT(identification_num) FROM history_of_trip where identification_num='""" + str(
                i[0]) + """' AND date>'""" + date2 + """'"""

            cur.execute(query)
            arr.append((cur.fetchall()[0][0], i[0]))

        arr.sort()
        count = math.ceil(arr.__len__() / 10)
        print("Car Id:")
        for i in range(0, count):
            print(arr[i][1])

        self.conn.close()

    #some changes in query8, we are finding number of customers using the same stations
    def query_8(self, date):

        time = datetime.datetime.strptime(date, "%Y-%m-%d")
        date_end = time - datetime.timedelta(days=30)
        self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
        cur = self.conn.cursor()
        query = """SELECT COUNT(username)
                   FROM history_of_charging NATURAL JOIN history_of_trip
                   WHERE history_of_charging.date<'""" + str(time).split(" ")[0] + """' and history_of_charging.date>'""" + str(date_end).split(" ")[0] + """' 
                   and starting_tr>starting_ch and ending_ch<ending_tr """

        self.conn.close()

    def query_9(self, date):
        time = datetime.datetime.strptime(date, "%Y-%m-%d") - datetime.timedelta(weeks=5)
        self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
        cur = self.conn.cursor()
        car_parts = dict()
        arr = []
        for i in range(5):
            query = """SELECT (COUNT(car_parts), car_parts)
            FROM history_of_repairing
            WHERE date>'""" + str(time).split(" ")[0] + """' 
            and date <'""" + str(time + datetime.timedelta(weeks=1)).split(" ")[0] + """' GROUP BY car_parts"""
            cur.execute(query)
            arr = cur.fetchall()
            for i in arr:
                arr2 = i[0].replace("(", "").replace(")", "").split(",")
                if car_parts.__contains__(arr2[1]):
                    car_parts[arr2[1]] += int(arr2[0])
                else:
                    car_parts[arr2[1]] = int(arr2[0])
                time = time + datetime.timedelta(weeks=1)

        for i in car_parts:
            car_parts[i] = car_parts[i] / 5
        print(car_parts)
        self.conn.close()
        #
        # def query_10(self, date):
        #     self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
        #     cur = self.conn.cursor()
        #     time_arr = [[7, 10], [12, 14], [17, 19]]
        #     car_amount = cur.execute("""SELECT COUNT(identification_num) FROM Car""")
        #     average_amount = [3][7]
        #     for i in range(7):
        #         for j in time_arr:
        #             query = """SELECT COUNT(identification_num)
        #                              FROM history_of_trip
        #                              WHERE starting_ch<""" + date + str(j[0]) + """ and
        #                              ending_ch>""" + date + str(j[1])
        #             average_amount[j][i] = cur.execute(query) / car_amount
        #
        #     morning = average_amount[0].sum() / 7
        #     afternoon = average_amount[1].sum() / 7
        #     evening = average_amount[2].sum() / 7
        #
        #     self.conn.close()


if __name__ == '__main__':
    db = DB()
    # db.delete_tables()
    # db.input_sample_data()
    db.query_9("2018-11-15")
    # db.query_8()
    # db.query_7()
    # db.query_6()
    # db.query_5()
    # db.query_4(2)
    # db.query_3('2018-11-24')
    # db.query_2("2018-11-26")
    # db.query_1(2)

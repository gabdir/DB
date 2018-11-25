import datetime
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
                UID SERIAL,
                Username SERIAL,
                Status VARCHAR(255) NOT NULL,
                Location POINT NOT NULL,
                Plate VARCHAR(10),
                company_id SERIAL NOT NULL,
                Color VARCHAR(10) NOT NULL,
                FOREIGN KEY (company_id) REFERENCES Company(company_id) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (UID) REFERENCES Station(uid) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (Username) REFERENCES Customer(username) ON UPDATE CASCADE ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE History_of_providing (
                WID SERIAL,
                PCompany_id SERIAL,
                Type_car_p VARCHAR(40), 
                FOREIGN KEY (PCompany_id) REFERENCES Provider(pcompany_id) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (WID) REFERENCES Workshops(wid) ON UPDATE CASCADE ON DELETE CASCADE,
                PRIMARY KEY(WID,PCompany_id)
            )
            """,
            """
            CREATE TABLE History_of_charging (
                Identification_num SERIAL,
                UID SERIAL,
                starting_ch TIME,
                ending_ch TIME,
                price DOUBLE PRECISION,
                FOREIGN KEY (Identification_num) REFERENCES Car(identification_num) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (UID) REFERENCES Station(uid) ON UPDATE CASCADE ON DELETE CASCADE,
                PRIMARY KEY(UID,Identification_num)
            )
            """,
            """
            CREATE TABLE History_of_trip (
                Identification_num SERIAL,
                Username SERIAL,
                starting_loc POINT,
                client_loc POINT,
                final_loc POINT,
                date DATE,
                starting_tr TIME,
                ending_tr TIME,
                FOREIGN KEY (Identification_num) REFERENCES Car(identification_num) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (Username) REFERENCES Customer(username) ON UPDATE CASCADE ON DELETE CASCADE,
                PRIMARY KEY(Username,Identification_num)
            )
            """,
            """
            CREATE TABLE History_of_repairing(
                Identification_num SERIAL,
                WID SERIAL,
                price DOUBLE PRECISION,
                Car_parts VARCHAR(40),
                date DATE,
                PRIMARY KEY (WID,Identification_num),
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
                        ('(26,76)', 'some2', '8-20', '1'),
                        ('(76,26)', 'some3', '8-20', '1'),
                        ('(76,76)', 'some4', '8-20', '1')
                    """,
                    """
                    INSERT INTO provider (phone_num, address, name)
                    VALUES ('977722677', 'Kazan', 'YaSuperProvider'),
                        ('977722678', 'Chelny', 'YaSuperProvider2')
                    """,
                    """
                    INSERT INTO customer (email, phone_number, location, full_name)
                    VALUES('hernya@mail.ru', '8777345621', '(231,129)', 'Cool Per'),
                    ('hernya2@mail.ru', '8777345622', '(179,35)', 'Cool Por')
                    """,
                    """
                    INSERT INTO car (model, status, location, plate, color, company_id)
                    VALUES ('CH11', 'used', '(123,43)', 'AN10200CS', 'red', '1'),
                        ('CH12', 'used', '(56,74)', 'AN10200CS', 'red', '1')
                    """)

                    # """
                    # INSERT INTO history_of_providing (wid, pcompany_id, type_car_p)
                    # VALUES ('1', '1', 'dich1'),
                    #     ('1', '1', 'dich2')
                    # """,
                    # """
                    # INSERT INTO history_of_charging (identification_num, uid, starting_ch, ending_ch, price)
                    # VALUES ('1', '1', '8:00', '18:00', '500')
                    # """,
                    # """
                    # INSERT INTO history_of_trip (identification_num, username, starting_loc, client_loc, final_loc)
                    # VALUES ('1', '1', (1, 5), (3, 8), (8, 9))
                    # """,
                    # """
                    # INSERT INTO history_of_repairing (identification_num, wid, price, car_parts, date)
                    # VALUES ('1', '1', '500', 'dich1', '2018.11.11')
                    # """,

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

    class select_queries():
        def query_1(self, username):
            query = """SELECT * FROM Car 
                    WHERE Color='red' AND 
                    position('AN' IN plate)=0 AND 
                    identification_num=(
                        SELECT identification_num FROM history_of_trip 
                        WHERE username=""" + username + """ AND 
                        date=""" + str(datetime.datetime.today()).split()[0] + """)
                """
            try:
                self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
                cur = self.conn.cursor()
                cur.execute(query)
                cur.close()
                self.conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)

            finally:
                self.conn.close()

        def query_2(self, date):
            for i in range(24):
                query ="""SELECT COUNT(identification_num) 
                          FROM history_of_charging 
                          WHERE starting_ch<""" + date + str(i + 1) + """ and 
                          ending_ch>""" + date + str(i)
                try:
                    self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
                    cur = self.conn.cursor()
                    count = cur.execute(query)
                    cur.close()
                    self.conn.commit()
                    print(count)
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)

                finally:
                    self.conn.close()

        def query_3(self, date):
            self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
            cur = self.conn.cursor()
            time_arr = [[7, 10], [12, 14], [17, 19]]
            car_amount = cur.execute("""SELECT COUNT(identification_num) FROM Car""")
            average_amount = [3][7]
            for i in range(7):
                for j in time_arr:
                    query = """SELECT COUNT(identification_num) 
                                     FROM history_of_trip 
                                     WHERE starting_tr<""" + date + str(j[0]) + """ and 
                                     ending_tr>""" + date + str(j[1])
                    average_amount[j][i] = cur.execute(query) / car_amount

            morning = average_amount[0].sum() / 7
            afternoon = average_amount[1].sum() / 7
            evening = average_amount[2].sum() / 7

            self.conn.close()

        def query_4(self,username):
            self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
            cur = self.conn.cursor()

            usr = cur.execute("""SELECT username FROM history_of_trip WHERE 
                                identification_num = 
                                (SELECT identification_num FROM history_of_charging HAVING count(*)>1)""")

            if usr != None and usr == username:
                print("Payment was doubled")
            else:
                print("No doubling")

            self.conn.close()

        def query_5(self, date):
            self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
            cur = self.conn.cursor()
            query = """SELECT starting_loc, final_loc, starting_tr, ending_tr
                        FROM history_of_trip
                        WHERE starting_tr>""" + date
            info = cur.execute(query)

            #Дописать средние значения
            self.conn.close()

        def query_6(self, date):
            self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
            cur = self.conn.cursor()
            time_arr = [[7, 10], [12, 14], [17, 19]]
            car_amount = cur.execute("""SELECT COUNT(client_loc), client_loc FROM history_of_trip""")
            average_amount = [3]
            for j in time_arr:
                query = """SELECT COUNT(client_loc), client_loc 
                    FROM history_of_trip
                    WHERE starting_tr<""" + date + str(j[0]) + """ and 
                    ending_tr>""" + date + str(j[1])
                average_amount[j] = cur.execute(query).sort();

            morning = average_amount[0][0]
            afternoon = average_amount[1][0]
            evening = average_amount[2][0]

            self.conn.close()

        def query_7(self, date):
            self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
            cur = self.conn.cursor()
            time_arr = [[7, 10], [12, 14], [17, 19]]
            car_amount = cur.execute("""SELECT COUNT(identification_num) FROM Car""")
            average_amount = [3][7]
            for i in range(7):
                for j in time_arr:
                    query = """SELECT COUNT(identification_num) 
                                     FROM history_of_trip 
                                     WHERE starting_ch<""" + date + str(j[0]) + """ and 
                                     ending_ch>""" + date + str(j[1])
                    average_amount[j][i] = cur.execute(query) / car_amount

            morning = average_amount[0].sum() / 7
            afternoon = average_amount[1].sum() / 7
            evening = average_amount[2].sum() / 7

            self.conn.close()

        def query_8(self, date):
            self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
            cur = self.conn.cursor()
            time_arr = [[7, 10], [12, 14], [17, 19]]
            car_amount = cur.execute("""SELECT COUNT(identification_num) FROM Car""")
            average_amount = [3][7]
            for i in range(7):
                for j in time_arr:
                    query = """SELECT COUNT(identification_num) 
                                     FROM history_of_trip 
                                     WHERE starting_ch<""" + date + str(j[0]) + """ and 
                                     ending_ch>""" + date + str(j[1])
                    average_amount[j][i] = cur.execute(query) / car_amount

            morning = average_amount[0].sum() / 7
            afternoon = average_amount[1].sum() / 7
            evening = average_amount[2].sum() / 7

            self.conn.close()

        def query_9(self, date):
            self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
            cur = self.conn.cursor()
            time_arr = [[7, 10], [12, 14], [17, 19]]
            car_amount = cur.execute("""SELECT COUNT(identification_num) FROM Car""")
            average_amount = [3][7]
            for i in range(7):
                for j in time_arr:
                    query = """SELECT COUNT(identification_num) 
                                     FROM history_of_trip 
                                     WHERE starting_ch<""" + date + str(j[0]) + """ and 
                                     ending_ch>""" + date + str(j[1])
                    average_amount[j][i] = cur.execute(query) / car_amount

            morning = average_amount[0].sum() / 7
            afternoon = average_amount[1].sum() / 7
            evening = average_amount[2].sum() / 7

            self.conn.close()

        def query_10(self, date):
            self.conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
            cur = self.conn.cursor()
            time_arr = [[7, 10], [12, 14], [17, 19]]
            car_amount = cur.execute("""SELECT COUNT(identification_num) FROM Car""")
            average_amount = [3][7]
            for i in range(7):
                for j in time_arr:
                    query = """SELECT COUNT(identification_num) 
                                     FROM history_of_trip 
                                     WHERE starting_ch<""" + date + str(j[0]) + """ and 
                                     ending_ch>""" + date + str(j[1])
                    average_amount[j][i] = cur.execute(query) / car_amount

            morning = average_amount[0].sum() / 7
            afternoon = average_amount[1].sum() / 7
            evening = average_amount[2].sum() / 7

            self.conn.close()

if __name__ == '__main__':
    db = DB()
    # db.delete_tables()
    db.input_sample_data()

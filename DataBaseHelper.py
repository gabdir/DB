import psycopg2


def create_tables():
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
            Time_charging TIME NOT NULL,
            Location POINT NOT NULL,
            Price_of_charging INTEGER NOT NULL,
            Plug_formats VARCHAR(255) NOT NULL,
            Free_sockets INTEGER NOT NULL,
            Amount_of_sockets INTEGER NOT NULL,
            company_id SERIAL REFERENCES Company(Company_id) ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE Workshops (
            WID SERIAL PRIMARY KEY,
            Location POINT NOT NULL,
            Available_car_p VARCHAR(255) NOT NULL,
            Available_time VARCHAR(255) NOT NULL,
            company_id SERIAL NOT NULL,
            FOREIGN KEY (company_id) REFERENCES Company(Company_id) ON UPDATE CASCADE ON DELETE CASCADE
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
        CREATE TABLE Car (
            Identification_num SERIAL PRIMARY KEY,
            Model VARCHAR(255) NOT NULL,
            UID SERIAL,
            Status VARCHAR(255) NOT NULL,
            Location POINT NOT NULL,
            company_id SERIAL NOT NULL,
            Color VARCHAR(10) NOT NULL,
            FOREIGN KEY (company_id) REFERENCES Company(Company_id) ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (UID) REFERENCES Station(UID) ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE Customer (
            Username VARCHAR(30) PRIMARY KEY,
            Email VARCHAR(20) NOT NULL,
            Phone_number VARCHAR(10) NOT NULL,
            Location POINT NOT NULL,
            Full_name VARCHAR(30) NOT NULL
        )

        """,
        """
        CREATE TABLE History_of_providing (
            WID SERIAL,
            PCompany_id SERIAL,
            Type_car_p VARCHAR(40),
            FOREIGN KEY (PCompany_id) REFERENCES Provider(PCompany_id) ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (WID) REFERENCES Workshops(WID) ON UPDATE CASCADE ON DELETE CASCADE,
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
            FOREIGN KEY (Identification_num) REFERENCES Car(Identification_num) ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (UID) REFERENCES Station(UID) ON UPDATE CASCADE ON DELETE CASCADE,
            PRIMARY KEY(UID,Identification_num)
        )
        """,
        """
        CREATE TABLE History_of_trip (
            Identification_num SERIAL,
            Username VARCHAR(30),
            starting_loc POINT,
            client_loc POINT,
            final_loc POINT,
            FOREIGN KEY (Identification_num) REFERENCES Car(Identification_num) ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (Username) REFERENCES Customer(Username) ON UPDATE CASCADE ON DELETE CASCADE,
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
            FOREIGN KEY (Identification_num) REFERENCES Car(Identification_num) ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (WID) REFERENCES Workshops(WID) ON UPDATE CASCADE ON DELETE CASCADE
        )
        """

    )
    conn = None
    try:
        conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
        cur = conn.cursor()

        '''''for command in commands2:
            cur.execute(command)'''''
        for command in commands:
            cur.execute(command)

        cur.close()

        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def delete_tables():
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
    conn = None
    try:
        conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
        cur = conn.cursor()

        '''''for command in commands2:
            cur.execute(command)'''''
        cur.execute(command)

        cur.close()

        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def input_sample_data():
    commands = ("""
    INSERT INTO company (company_id, company_name) 
    VALUES ('Jane', '1935-08-01')
    """,
                """
                INSERT INTO station (time_charging, location, price_of_charging, plug_formats, free_sockets, amount_of_sockets) 
                values ('1:00', 'Kazan', '100', 'first', '5', '7'),
                    ('3:00', 'Kazan', '300', 'first', '5', '7')
                """,
                """
                INSERT INTO workshops (location, available_car_p, available_time, company_id) 
                values ('Kazan', 'some1', '100', '1'),
                    ('Kazan', 'some2', '200', '2')
                """,
                """
                INSERT INTO provider (phone_num, address, name) 
                values ('977722677', 'Kazan', 'YaSuperProvider'),
                    ('977722678', 'Kazan', 'YaSuperProvider')
                """,
                """
                INSERT INTO car (model, uid, status, location, company_id) 
                values ('CH11', '1', 'used', 'Kazan', '1'),
                    ('CH12', '2', 'used', 'Kazan', '1'),
                    ('CH13', '3', 'used', 'Kazan', '2')
                """,
                """
                INSERT INTO customer (email, phone_number, location, full_name) 
                values ('hernya@mail.ru', '8777345621', 'Kazan', 'cool per'),
                    ('hernya2@mail.ru', '8777345622', 'Kazan', 'cool por')
                    """,
                """
                INSERT INTO history_of_providing (wid, pcompany_id, type_car_p) 
                values ('1', '1', 'dich1'),
                    ('1', '1', 'dich2')
                """,
                """
                INSERT INTO history_of_charging (identification_num, uid, starting_ch, ending_ch, price) 
                values ('1', '1', '8:00', '18:00', '500')
                """,
                """
                INSERT INTO history_of_trip (identification_num, username, starting_loc, client_loc, final_loc) 
                values ('1', '1', (1, 5), (3, 8), (8, 9))
                """,
                """
                INSERT INTO history_of_repairing (identification_num, wid, price, car_parts, date) 
                values ('1', '1', '500', 'dich1', '2018.11.11')
                """,
                )
    conn = None
    try:
        conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
        cur = conn.cursor()

        '''''for command in commands2:
            cur.execute(command)'''''
        cur.execute(commands)

        cur.close()

        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    delete_tables()
    create_tables()

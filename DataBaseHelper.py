
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
            Time_charing INTEGER NOT NULL,
            Location VARCHAR(255) NOT NULL,
            Price_of_charging INTEGER NOT NULL,
            Plug_formats VARCHAR(255) NOT NULL,
            Free_sockets INTEGER NOT NULL,
            Amount_of_sockets INTEGER NOT NULL,
            company SERIAL REFERENCES Company(Company_id) ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE Car (
            Identification_num SERIAL PRIMARY KEY,
            Model VARCHAR(255) NOT NULL,
            Status VARCHAR(255) NOT NULL,
            Location SERIAL NOT NULL,
            c_company SERIAL NOT NULL,
            FOREIGN KEY (c_company) REFERENCES Company(Company_id) ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE Workshops (
            WID SERIAL PRIMARY KEY,
            Location VARCHAR(255) NOT NULL,
            Available_car_p VARCHAR(255) NOT NULL,
            Available_time DOUBLE PRECISION NOT NULL,
            w_company SERIAL NOT NULL,
            FOREIGN KEY (w_company) REFERENCES Company(Company_id) ON UPDATE CASCADE ON DELETE CASCADE
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
        CREATE TABLE Payment (
            PCompany_id SERIAL,
            Company_id SERIAL,
            FOREIGN KEY (Company_id) REFERENCES Company(Company_id) ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (PCompany_id) REFERENCES Provider(PCompany_id) ON UPDATE CASCADE ON DELETE CASCADE     
        )
        """
    )
    conn = None
    try:
        conn = psycopg2.connect("dbname='postgres' user='test' host='10.90.138.41' password='test'")
        cur = conn.cursor()

        for command in commands:
            cur.execute(command)

        cur.close()

        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
        create_tables()
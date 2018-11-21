
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
                company VARCHAR(255) REFERENCES Company(Company_id)
                )
        """)
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
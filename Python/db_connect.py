import psycopg2
from decouple import config



def db_connect():
    '''Boilerplate, connect to PostgreSQL database'''
    conn = None

    try:
        # Create connection to DB
        conn = psycopg2.connect(dbname=config('DATABASE'),\
                                user=config('DB_USER'),\
                                password=config('DB_PASSWORD'),\
                                host=config('HOST'),\
                                port=config('DB_PORT'))

        # Create a cursor
        cur = conn.cursor()

        # EXAMPLE: create SQL scripts with cur.execute("")
        # =================================
        create_script = '''CREATE TABLE accounts ( 
            user_id serial PRIMARY KEY,
            username VARCHAR ( 50 ) UNIQUE NOT NULL, 
            password VARCHAR ( 50 ) NOT NULL, 
            email VARCHAR ( 255 ) UNIQUE NOT NULL, 
            created_on TIMESTAMP NOT NULL,
                last_login TIMESTAMP 
        );'''
        cur.execute(create_script)
        print(f'Script has been executed')
        # =================================
        # # execute a statement
        # print('PostgreSQL database version:')
        # cur.execute('SELECT version()')

        # # display the PostgreSQL database server version
        # db_version = cur.fetchone()
        # print(db_version)
        # =================================
        # Close the cursor
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        # Close connection to DB
        if conn is not None:
            conn.close()
            print(f'The connection to DB is closed')

if __name__ == "__main__":
    db_connect()
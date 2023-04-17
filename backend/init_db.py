import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host="localhost",
    database="thesis_db",
    user=os.getenv('DB_USERNAME'),
    password=os.getenv('DB_PASSWORD')
)

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS rooms;')
cur.execute('CREATE TABLE rooms (number integer PRIMARY KEY,'
            'type integer NOT NULL,'
            'tenant1 real[] default \'{}\','
            'tenant2 real[] default \'{}\','
            'tenant3 real[] default \'{}\','
            'tenant4 real[] default \'{}\','
            'tenant5 real[] default \'{}\''
            ')'
            )

conn.commit()

cur.close()
conn.close()

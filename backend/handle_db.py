import os
import random
from typing import List
import psycopg2
from dotenv import load_dotenv
import pickle as pk

load_dotenv()
clusters = pk.load(open("cluster_centers.pkl", 'rb'))


def add(room_number: int, room_type: int, tenant: List[float]) -> bool:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="thesis_db",
            user=os.getenv('DB_USERNAME'),
            password=os.getenv('DB_PASSWORD')
        )

        curr = conn.cursor()
        postgreSQL_select_query = f"select * from rooms where number={room_number};"

        curr.execute(postgreSQL_select_query)

        if curr.rowcount == 0:
            tenant_postgres_array = "".join(str(v) + "," for v in tenant)
            tenant_postgres_array = tenant_postgres_array[:-1]
            postgreSQL_insert_query = f"INSERT INTO rooms(number, type, tenant1, tenant2, tenant3, tenant4, tenant5) VALUES ({room_number}, {room_type}, \'{{{tenant_postgres_array}}}\', \'{{}}\', \'{{}}\', \'{{}}\', \'{{}}\');"

            curr.execute(postgreSQL_insert_query)
            conn.commit()
            curr.close()
            conn.close()
            return True

        room = curr.fetchone()

        length = 2 + (room[1] * 3)
        postgreSQL_update_query = f"UPDATE rooms SET "
        added = False

        for i in range(2, 2 + length):
            if room[i] == []:
                tenant_postgres_array = "".join(str(v) + "," for v in tenant)
                tenant_postgres_array = tenant_postgres_array[:-1]
                postgreSQL_update_query += f"tenant{i - 1}=\'{{{tenant_postgres_array}}}\'"
                added = True
                break

        postgreSQL_update_query += f" WHERE number={room_number};"

        if added:
            curr.execute(postgreSQL_update_query)

        conn.commit()

        curr.close()
        conn.close()

        return added

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
        return False


def getAllRooms() -> List[tuple]:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="thesis_db",
            user=os.getenv('DB_USERNAME'),
            password=os.getenv('DB_PASSWORD')
        )

        curr = conn.cursor()
        postgreSQL_select_query = f"select * from rooms;"

        curr.execute(postgreSQL_select_query)

        rooms = curr.fetchall()
        conn.commit()

        curr.close()
        conn.close()
        return rooms

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
        return []


def populateDatabase(type0_rooms: int, type1_rooms: int) -> bool:
    try:
        for i in range(type0_rooms):
            tenant = clusters[random.randint(0, len(clusters) - 1)]
            add(i, 0, tenant=tenant)
        for i in range(type0_rooms, type0_rooms + type1_rooms):
            count = 4
            while count:
                count -= 1
                tenant = clusters[random.randint(0, len(clusters) - 1)]
                add(i, 1, tenant=tenant)
        return True
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
        return False


if __name__ == "__main__":
    #populateDatabase(50, 50)
    # print(getAllRooms())
    pass

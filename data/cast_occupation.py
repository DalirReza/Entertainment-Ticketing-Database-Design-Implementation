import random
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="(Al1)withoutgravity",
    database="Tiwall"
)


# Event_ID extraction
curser = mydb.cursor()
query = """SELECT Event_ID FROM event;"""
curser.execute(query)
records = curser.fetchall()
Event_IDs = [record[0] for record in records]
curser.close()


curser = mydb.cursor()
query = """SELECT Cast_ID FROM cast;"""
curser.execute(query)
records = curser.fetchall()
Cast_IDs = [record[0] for record in records]
curser.close()

sql = """INSERT INTO cast_occupation (Cast_ID, Event_ID, Occupation)
VALUES (%s, %s, %s)"""

for event_id in Event_IDs:
    for i in range(random.randint(2, 5)):
        curser = mydb.cursor()
        Cast_ID = random.choice(Cast_IDs)
        datas = [Cast_ID, event_id, random.choice(["Singer", 'Director', 'actor', 'manager', 'writer'])]
        curser.execute(sql, datas)
        mydb.commit()
        curser.close()
        
mydb.close()
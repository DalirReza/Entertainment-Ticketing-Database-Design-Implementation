import random
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="(Al1)withoutgravity",
  database="Tiwall"
)

def random_date():
    year = "2024"
    month = str(random.randint(2,12))
    if (len(month) == 1):
        month = "0" + month
    day = str(random.randint(1, 27))
    if len(day) == 1:
        day = "0" + day
    return "-".join([year, month, day])



# Event_ID extraction
curser = mydb.cursor()
query = """SELECT Event_ID FROM event;"""
curser.execute(query)
records = curser.fetchall()
Event_IDs = [record[0] for record in records]
curser.close()
print(Event_IDs)


# session
sql = """INSERT INTO session(Event_ID, Start_time, End_time, Date)
VALUES(%s, %s, %s, %s)"""
for i in range(len(Event_IDs)):
    for j in range(random.randint(2, 5)):
        curser = mydb.cursor()
        date = random_date()
        start_time = str(random.randint(12, 20)) + ":00:00"
        datas = [Event_IDs[i], start_time, None, date]
        print(datas)
        curser.execute(sql, datas)
        mydb.commit()
        curser.close()


mydb.close()

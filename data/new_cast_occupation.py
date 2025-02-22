import mysql.connector
from faker import Faker
import random
from datetime import date, timedelta

fake = Faker('fa_IR')
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='tiwall'
)
cursor = conn.cursor()

event_id = list(range(227, 229)) + list(range(321, 331))
for i in range(12):
    id = event_id[i]
    cast_id = 263 + i
    occupation = random.choice(["برگزار کننده", "هماهنگی"])

    cursor.execute('''
    INSERT INTO `cast_occupation` (`Cast_ID`, `Event_ID`, `Occupation`)
    VALUES (%s, %s, %s)
    ''', (cast_id, id, occupation))

conn.commit()
conn.close()
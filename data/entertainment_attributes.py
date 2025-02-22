# Generate and insert random data for the education table
import mysql.connector
from faker import Faker
import random
from datetime import date, timedelta

fake = Faker('fa_IR')
# Replace 'your_host', 'your_username', 'your_password', and 'your_database' with your MySQL server details
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='tiwall'
)

cursor = conn.cursor()


for event_id in range(331, 334):
    instructor = fake.name()
    presenter = fake.name()
    presenter_phone = fake.phone_number()

    cursor.execute('''
    INSERT INTO `exhibit` (`Event_ID`, `Instructor`, `Presenter`, `Presenter_phone`)
    VALUES (%s, %s, %s, %s)
    ''', (event_id, instructor, presenter, presenter_phone))

conn.commit()
conn.close()
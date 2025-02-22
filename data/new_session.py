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

from datetime import datetime, timedelta

for event_id in range(230, 271):
    for _ in range(2):

        datetime_between = fake.date_time_between(start_date='-2y', end_date='now', tzinfo=None)
        start_time = datetime_between.time()

        # Calculate end time as 1 to 2.5 hours after start time
        end_time = (datetime.combine(datetime.today(), start_time) + timedelta(hours=random.uniform(1, 2.5))).time()

        date = datetime_between.date()

        cursor.execute('''
        INSERT INTO `session` (`Event_ID`, `Start_time`, `End_time`, `Date`)
        VALUES (%s, %s, %s, %s)
        ''', (event_id, start_time, end_time, date))

conn.commit()
conn.close()
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


# Generate and insert 100 rows of data for the cast table
for _ in range(12):
    first_name = fake.first_name()
    last_name = fake.last_name()

    cursor.execute('''
    INSERT INTO `cast` (`First_name`, `Last_name`)
    VALUES (%s, %s)
    ''', (first_name, last_name))

conn.commit()
conn.close()
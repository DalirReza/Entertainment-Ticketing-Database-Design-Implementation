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

for event_id in range(311, 321):
    instructor = fake.name()
    presenter = random.choice(['آرمان', 'الناز', 'سامان', 'نیلوفر'])
    presenter_phone = fake.phone_number()
    category = random.choice(['پژوهشی', 'نوجوان', 'عکاسی', 'علم و فناوری'])
    genre = random.choice(['بومی', 'روانشناسی', 'اجتماعی', 'فلسفی'])

    cursor.execute('''
    INSERT INTO `education` (`Event_ID`, `Instructor`, `Presenter`, `Presenter_phone`, `Category`, `Genre`)
    VALUES (%s, %s, %s, %s, %s, %s)
    ''', (event_id, instructor, presenter, presenter_phone, category, genre))

conn.commit()
conn.close()
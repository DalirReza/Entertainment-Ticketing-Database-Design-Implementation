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

for site_no in range(1, 11):
    address = fake.address()
    phone = fake.phone_number()
    
    # Generate a fake latitude and longitude
    latitude = fake.latitude()
    longitude = fake.longitude()
    
    location = f'https://www.google.com/maps?q={latitude},{longitude}'

    cursor.execute('''
    UPDATE `site`
    SET `Address` = %s, `Phone` = %s, `Location` = %s
    WHERE `Site_no` = %s
    ''', (address, phone, location, site_no))

conn.commit()
conn.close()
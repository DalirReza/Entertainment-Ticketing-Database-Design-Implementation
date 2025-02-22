import random
from faker import Faker
import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="tiwall"
)

cursor = db_connection.cursor()

def generate_photo_fake_data():
    fake = Faker()

    for _ in range(100):
        event_id = random.randint(212, 230)
        
        # Generate a more realistic photo link with a common photo hosting domain
        photo_hosting_domain = random.choice(['instagram.com', 'flickr.com', '500px.com'])
        photo_id = fake.uuid4().split('-')[0]  # Using part of a UUID as a photo ID
        link = f"https://{photo_hosting_domain}/{photo_id}"

        sql = f"INSERT INTO photo (Event_ID, Link) VALUES ({event_id}, '{link}')"
        cursor.execute(sql)

    db_connection.commit()

generate_photo_fake_data()

cursor.close()
db_connection.close()
file_path = '.\hi.txt'
with open(file_path, 'r') as file:
    usernames_list = [line.strip() for line in file.readlines()]



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

def generate_random_data(num_rows=500):
    comments = []

    for _ in range(num_rows):
        comment = {
            'Username': random.choice(usernames_list),
            'Event_ID': random.randint(212, 230),
            'Date': fake.date_between(start_date='-4y', end_date='today'),
            'Type': random.choice(['Review', 'Dialog']),
            'Context': fake.paragraph(),
            'Point': random.randint(1, 5) 
        }
        comments.append(comment)

    return comments

def insert_data(data):
    for comment in data:
        cursor.execute("""
            INSERT INTO `comment` (`Username`, `Event_ID`, `Date`, `Type`, `Context`, `Point`)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (comment['Username'], comment['Event_ID'], comment['Date'], comment['Type'], comment['Context'], comment['Point']))

    conn.commit()

if __name__ == "__main__":
    comments_data = generate_random_data()
    insert_data(comments_data)

    cursor.close()
    conn.close()
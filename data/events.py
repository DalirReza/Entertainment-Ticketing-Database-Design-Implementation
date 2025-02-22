import mysql.connector
from faker import Faker
import random

# Function to generate random Persian text using faker
def generate_persian_text():
    fake = Faker('fa_IR')
    return fake.text()

# MySQL connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'tiwall'
}

# Function to insert data into the event table
def insert_data(cursor, event_type, name, duration, price, discount, salary):
    explanation = generate_persian_text()
    summary = generate_persian_text()
    regulation = generate_persian_text()

    sql = """
    INSERT INTO `event` (`Event_type`, `Name`, `Duration`, `Price`, `Discount`, `Salary`, `Explanation`, `Summary`, `Regulation`)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (event_type, name, duration, price, discount, salary, explanation, summary, regulation)

    cursor.execute(sql, values)

# Connect to MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# List of event names
event_names = ["ضیافت شام برای احمق ها", "خاطرات خانه ای که نیست", "خرس", "آنتیگونه", "هملت",
               "باغ وحش شیشه ای", "سلام خداحافظ", "بی خبران حیرانند", "دوزخی ها", "یونسکو شدن"]

for i in range(10):
    event_type = random.choice(['theatre', 'radio_theatre'])
    name = event_names[i]
    duration = round(random.uniform(0.5, 2.5), 2)
    price = random.choice([100000, 120000, 160000, 150000, 200000, 80000])
    discount = random.choice([None, 10, 15, 25])
    salary = random.choice([None, 9])

    insert_data(cursor, event_type, name, duration, price, discount, salary)

conn.commit()
conn.close()
import mysql.connector
from random import randint, choice

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="tiwall"
)

# Create a cursor to execute SQL queries
cursor = db.cursor()

# Number of sessions and data to generate for each session
num_sessions = 100
data_per_session = 15

# Possible values for the 'Status' column
# 0 : available
# 1 : sold
status_options = [0, 1, 1, 1]

# Generate data for each session
for session_no in range(1, num_sessions + 1):
    hall_no = randint(1,20)
    for i in range(data_per_session):
        status = choice(status_options)
        price = None  # Assuming 'price' is set to NULL

        seat_no = (hall_no - 1)*15 + 3542 + i

        sql = "INSERT INTO seat_status (Seat_no, Session_no, Status, Price) VALUES (%s, %s, %s, %s)"
        values = (seat_no, session_no, status, price)

        cursor.execute(sql, values)
        db.commit()
    
cursor.close()
db.close()
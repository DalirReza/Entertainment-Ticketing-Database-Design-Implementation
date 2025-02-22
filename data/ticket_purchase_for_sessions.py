import mysql.connector
import random

from datetime import datetime, timedelta
# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="tiwall"
)

# Create a cursor to execute SQL queries
cursor = db.cursor()


file_path = '.\hi.txt'
with open(file_path, 'r') as file:
    usernames_list = [line.strip() for line in file.readlines()]


# Define the session number
for session_no in range(1, 101) :

    # Execute the query to count rows with Status = 'available' and Session_no = 1
    sql = "SELECT Seat_no FROM seat_status WHERE Status = 1 AND Session_no = %s"
    values = (session_no,)
    cursor.execute(sql, values)
    # Fetch the result
    results = cursor.fetchall()
    seats = list()
    for j in range (len(results)) :
        seats.append(results[j][0])

    backup = seats
    # Define the session number
    session_no_to_search = session_no
    # Execute the query to retrieve Event_ID for the specified session_no
    sql = "SELECT Event_ID FROM session WHERE Session_no = %s"
    values = (session_no_to_search,)
    cursor.execute(sql, values)
    # Fetch the result
    the_event_id = cursor.fetchone()[0]
    with open(file_path, 'r') as file:
      temp_username = [line.strip() for line in file.readlines()]

    print(len(temp_username))

    while len(seats) != 0:
        new_count = random.randint(1,len(seats))
        new_count = random.randint(1, new_count)
    
        sql = "SELECT Price FROM event WHERE Event_ID = %s"
        values = (the_event_id,)
        cursor.execute(sql, values)
        # Fetch the result
        price_each = cursor.fetchone()[0]

        expense = price_each * new_count

        user = temp_username.pop(random.randint(1,len(temp_username)-1))
        
        date_range_start = datetime(2023, 1, 1)  # Start of the date range
        date_range_end = datetime(2023, 12, 31)  # End of the date range
        random_date = date_range_start + timedelta(days=random.randint(0, (date_range_end - date_range_start).days))

        sql = "INSERT INTO purchase (Username, Event_ID, Date, Ticket_count, Expense) VALUES (%s, %s, %s, %s, %s)"
        values = (user, the_event_id, random_date, new_count, expense)

        cursor.execute(sql, values)

        last_inserted_id = cursor.lastrowid

        # Print the last inserted ID
        print(f"Last Inserted ID: {last_inserted_id}")
        for k in range(new_count) :
            sql = "INSERT INTO ticket (seat_no, session_no, track_no) VALUES (%s, %s, %s)"
            values = (seats.pop(0), session_no, last_inserted_id)
            cursor.execute(sql, values)

    db.commit()

cursor.close()
db.close()
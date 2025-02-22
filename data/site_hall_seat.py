import random
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="(Al1)withoutgravity",
  database="Tiwall"
) 


pr = ["Tehran",
    "Isfahan",
    "Fars",
    "Kerman",
    "Mazandaran",
    "Gilan",
    "Golestan",
    "Hamedan",
    "Ardabil",
    "Bushehr"]

# site
for i in range(1, 11):
    mycursor = mydb.cursor()
    datas = (i, pr[i-1], None, None, None, None)
    sql = '''INSERT INTO site (Site_no, Province, City, Address, Phone, Location)
    VALUES (%s, %s, %s, %s, %s, %s)'''

    mycursor.execute(sql, datas)
    mydb.commit()
    mycursor.close()


# hall
for i in range(1, 11):
    for j in range(1, 3):
        mycursor = mydb.cursor()
        datas = (2*(i-1) + j, i, j)
        sql = '''INSERT INTO hall (Hall_no, Site_no, Hall_number)
        VALUES (%s, %s, %s)'''
    
        mycursor.execute(sql, datas)
        mydb.commit()
        mycursor.close()

# seat
for hall_no in range(1, 21):
    for row in range(1, 4):
        for num in range(1, 6):
            mycursor = mydb.cursor()
            datas = (hall_no, "0", row, num)
            sql = '''INSERT INTO seat (Hall_no, Floor, Row_no, Seat_number)
            VALUES (%s, %s, %s, %s)'''
        
            mycursor.execute(sql, datas)
            mydb.commit()
            mycursor.close()

mydb.close()
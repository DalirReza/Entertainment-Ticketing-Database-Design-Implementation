import mysql.connector
  

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="(Al1)withoutgravity",
  database="Tiwall"
) 
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
 
for x in mycursor:
  print(x) 

sql = '''INSERT INTO event (Event_type, Name, Duration, Price, Discount, Salary, Instructor, Presenter, Presenter_phone, Catergory, Genre, Explanation, Summary, Regulation) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

val = ("concert", "SOOSAN", 2, 920000, 0, 9, None, None, None, "GOOD", "NOT BAD", None, None, None)
mycursor.execute(sql, val)
mydb.commit()
mydb.close()
print(mycursor.rowcount, "record inserted.")

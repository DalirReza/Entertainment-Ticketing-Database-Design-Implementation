from faker import *
import random
import string
import mysql.connector

f = Faker()

def generate_username(n):
    random_string = ''.join(random.choices(string.ascii_lowercase, k=n))
    unique_identifier = str(random.randint(1000, 9999))
    username = random_string + unique_identifier
    return username

def generate_pass(n):
    random_string = ''.join(random.choices(string.ascii_lowercase, k=n))
    unique_identifier = str(random.randint(100, 99999))
    username = random_string + unique_identifier
    return username

def generate_phone():
    return str(random.randint(100000000, 999999999))
    
def balance():
    return random.randint(0, 500000000)

def educational_degree():
    return random.choice(["Diploma", "Bachelor", "Master", "Ph.D."])

def random_major():
    l = ['Computer Science',
        'Electrical Engineering',
        'Mechanical Engineering',
        'Civil Engineering',
        'Biology',
        'Chemistry',
        'Physics',
        'Mathematics',
        'Economics',
        'Psychology',
        'Sociology',
        'Political Science',
        'English Literature',
        'History',
        'Business Administration',
        'Nursing',
        'Architecture',
        'Environmental Science',
        'Graphic Design',
        'Linguistics']
    
    return random.choice(l)

def random_province():
    pr = ["Tehran",
        "Isfahan",
        "Fars",
        "Razavi Khorasan",
        "East Azerbaijan",
        "West Azerbaijan",
        "Khuzestan",
        "Kerman",
        "Mazandaran",
        "Gilan",
        "Lorestan",
        "Golestan",
        "Hamedan",
        "Yazd",
        "Markazi",
        "Ardabil",
        "Bushehr",
        "Hormozgan",
        "Kermanshah",
        "Kurdistan"]
    
    return random.choice(pr)

def random_city():
    ct = ["Tehran",
        'Karaj',
        'Eslamshahr',
        'Isfahan',
        'Shahin Shahr',
        'Najafabad',
        'Shiraz',
        'Marvdasht',
        'Jahrom',
        'Mashhad',
        'Sabzevar',
        'Neyshabur',
        'Tabriz',
        'Maragheh',
        'Kaleybar',
        'Urmia',
        'Khoy',
        'Mahabad',
        'Ahvaz',
        'Abadan',
        'Dezful',
        'Kerman',
        'Rafsanjan',
        'Sirjan',
        'Sari',
        'Babol',
        'Amol',
        'Rasht',
        'Bandar-e Anzali',
        'Lahijan',
        'Tehran',
        'Karaj',
        'Eslamshahr',
        'Isfahan',
        'Shahin Shahr',
        'Najafabad',
        'Shiraz',
        'Marvdasht',
        'Jahrom',
        'Mashhad',
        'Sabzevar',
        'Neyshabur',
        'Tabriz',
        'Maragheh',
        'Kaleybar']
    
    return random.choice(ct)

def random_date():
    year = str(random.randint(2005, 2023))
    month = random.randint(1, 12)
    if (1 <= month <= 9):
        month = "0" + str(month)
    month = str(month)
    if (month == "02"):
        day = random.randint(1, 27)
    else:
        day = random.randint(1, 30)
    if (1 <= day <= 9):
        day = "0" + str(day) 
    day = str(day)
    return  "-".join([year, month, day])

usernames = list()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="(Al1)withoutgravity",
  database="Tiwall"
) 

for i in range(1500):
    mycursor = mydb.cursor()
    full_name = f.name().split(" ")
    first_name, last_name = full_name[0], full_name[1] 
    user_name = generate_username(6)
    while (user_name in usernames):
        user_name = generate_username(6)
    visible_name = full_name[0] + " " + full_name[1]
    phone = "09" + generate_phone()
    wallet_balance = balance()
    password = generate_pass(9)
    education = educational_degree()
    major = random_major()
    profile = None
    occupation = None
    joining_date = random_date()
    bio = None
    province = random_province()
    city = random_city()
    address = None
    postal_code = None
    plus = random.randint(0, 1)
    
    
    sql = '''INSERT INTO user_account (Username, First_name, Last_name, Visible_name, Phone, Wallet_balance, Password, Educational_degree, Major, Profile, Occupation, Joining_date, Bio, Province, City, Address, Postal_code, Plus) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    val = (user_name, first_name, last_name, visible_name, phone, wallet_balance, password, education, major, profile,  occupation, joining_date, bio, province, city, address, postal_code, plus)
    # print(*val, sep="\n")
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

mydb.close()
print(mycursor.rowcount, "record inserted.")
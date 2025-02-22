from unidecode import unidecode
import mysql.connector


file = open("events.txt")
lines = file.readlines()
file.close()

idx = 0
while (idx < len(lines)):
    if lines[idx] == "\n":
        lines.pop(idx)
    else:
        idx += 1

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="(Al1)withoutgravity",
  database="Tiwall"
) 


# print(ord('۱'))
# print(ord('۲'))
# print(ord('1'))
    
def digits_extractor(s):
    idx = 0
    ans = str()
    while (idx < len(s)):
        if (48 <= ord(s[idx]) <= 57):
            ans += s[idx]
        elif (1776 <= ord(s[idx]) <= 1785):
            ans += unidecode(s[idx])   
        idx += 1 
    return ans

def general_(s):
    s = s[:-1]
    return s

def duration_correcter(s : str):
    if ("دقیقه" in s):
        return str(int(int(digits_extractor(s))/60))
    elif ("ساعت" in s and "دقیقه" in s):
        t = s.split(" ")
        return str(int(digits_extractor(t[0])) + int(digits_extractor(t[2])))
    elif ("ساعت" in s):
        return str(int(digits_extractor(s)))
    else:
        return "0"

def price_corrector(s):
    idx = 0
    ans = str()
    while (idx < len(s)):
        if (s[idx] == "0"):
            break
        ans += s[idx]
        idx += 1
    
    while (idx < len(s) and s[idx] == "0"):
        ans += '0'
        idx += 1
        
    return ans
    

def discount_corrector(s : str):
    if ("NULL" in s or digits_extractor(s) == ""):
        return "0"
    else:
        return digits_extractor(s)

idx = 0
while(idx != len(lines)):
    
    # Event_ID = general_(lines[idx])
    # print(lines[idx])
    # print(Event_ID)
    Event_type = general_(lines[idx+1])
    Name = general_(lines[idx+2])
    # print(Name)
    Duration = duration_correcter(lines[idx+3])
    Price = price_corrector(digits_extractor(lines[idx+4]))
    print("-" + lines[idx+5] + "-")
    Discount = discount_corrector(lines[idx+5])
    print("+" + Discount + "+")
    Salary = "9"
    Instructor = general_(lines[idx+7])
    Presenter = general_(lines[idx+8])
    Presenter_phone = digits_extractor(lines[idx+9])
    Genre = general_(lines[idx+10])
    Category = general_(lines[idx+11])
    Explanation = general_(lines[idx+12])
    Summary = general_(lines[idx+13])
    Regulation = general_(lines[idx+14])
    idx += 16
    
    datas = list((Event_type, Name, Duration, Price, Discount, Salary, Instructor, Presenter, Presenter_phone,
          Category, Genre, Explanation, Summary, Regulation))

    
    # print(*datas, sep="\n")

    # for i in range(15):
    #     if (i in [3, 4, 5, 6, 9]):
    #         datas[i] = make_it_tidy(datas[i])
    #     else:
    #         datas[i] = datas[i][:-1]
    
    # datas[4] = price_detector(datas[4])

    # print("--------------------")

    mycursor = mydb.cursor()
    sql = '''INSERT INTO event (Event_type, Name, Duration, Price, Discount, Salary, Instructor, Presenter, Presenter_phone,
          Category, Genre, Explanation, Summary, Regulation)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

    mycursor.execute(sql, datas)
    mydb.commit()
    mycursor.close()



mydb.close()
print(mycursor.rowcount, "record inserted.")

    
    

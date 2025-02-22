import random
import mysql.connector
from time import sleep

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="(Al1)withoutgravity",
    database="Tiwall"
)

people_ = """Farhad Khosravi - Film Director
Sahar Rahimi - Actress
Amir Hosseini - Screenwriter
Nasrin Jafari - Theater Director
Reza Mahmoudi - Cinematographer
Leila Sadeghi - Music Composer
Mehran Salehi - Actor
Parisa Azimi - Costume Designer
Arash Mousavi - Film Producer
Shadi Esfahani - Set Designer
Sina Ahmadi - Sound Engineer
Maryam Taghavi - Casting Director
Ali Rostami - Stage Manager
Neda Mirzaei - Makeup Artist
Kian Akbari - Assistant Director
Laleh Abbasi - Choreographer
Behzad Amini - Script Supervisor
Sanaz Bahrami - Lighting Designer
Hamed Khodabakhshi - Stunt Coordinator
Roya Farzaneh - Film Editor
Ehsan Jalali - Special Effects Supervisor
Elham Nasiri - Publicist
Babak Ghasemi - Production Designer
Zahra Sadeghi - Playback Singer
Reza Yavari - Film Critic
Sara Khadem - Costume Assistant
Hamid Ghaffari - Theater Actor
Parvaneh Eskandari - Concert Pianist
Ali Asghari - Talent Agent
Mitra Rahmani - Film Distributor
Peyman Fathi - Theatre Producer
Mahsa Farrokhi - Assistant Costume Designer
Amin Mohammadi - Dialogue Coach
Fatemeh Amirpour - Casting Assistant
Reza Farhadi - Concert Promoter
Saba Behzadi - Documentary Filmmaker
Amir Aliabadi - Music Video Director
Sepideh Davoodi - Voice Actor
Mohammad Gharib - Stand-up Comedian
Parham Akhavan - Digital Effects Artist
Hengameh Javadi - Foley Artist
Nader Afshar - Film Location Scout
Marjan Rahimi - Film Festival Organizer
Ali Rezai - Talent Manager
Mojgan Alizadeh - Film Archivist
Armin Ahmadi - Film Distribution Manager
Zahra Daryani - Concert Lighting Technician
Behnam Mirzaei - Concert Sound Technician
Mahtab Yazdani - Documentary Producer
Hamideh Farahani - Music Festival Coordinator"""

people = """Asghar Farhadi - Director
Majid Majidi - Director
Abbas Kiarostami - Director
Bahram Beyzaie - Director
Rakhshan Bani-Etemad - Director
Samira Makhmalbaf - Director
Jafar Panahi - Director
Marzieh Boroumand - Director
Narges Abyar - Director
Mani Haghighi - Director
Googoosh - Singer
Ebi - Singer
Dariush Eghbali - Singer
Mahasti - Singer
Moein - Singer
Hayedeh - Singer
Shadmehr Aghili - Singer
Leila Forouhar - Singer
Mansour - Singer
Andy - Singer
Shahab Hosseini - Actor
Golshifteh Farahani - Actress
Taraneh Alidoosti - Actress
Leila Hatami - Actress
Homayoun Ershadi - Actor
Hanieh Tavassoli - Actress
Peyman Maadi - Actor
Nazanin Boniadi - Actress
Behrouz Vossoughi - Actor
Sarah Bayat - Actress"""

people_name = [(item.split(" - "))[0] for item in people.splitlines()]
# people_occupation = [(item.split(" - "))[1] for item in people]

# seat_status
query = """INSERT INTO cast (First_name, Last_name)
VALUES(%s, %s);"""
  
for person in people_name:
    print(person)
    curser = mydb.cursor()
    if (" " in person):
      first, last = person.split(" ")
    else:
      first = person
      last = None
    curser.execute(query, (first, last))
    mydb.commit()
    curser.close()


mydb.close()
import random
myFile = open("purchase.txt", 'a', encoding="utf-8")

ids = []
for i in range(50):
    myFile.write(str(random.randint(1000000000, 10000000000)))
    myFile.write('\n')
    myFile.write(str(i))
    myFile.write('\n')
    myFile.write(str(random.randint(1, 100)))
    myFile.write('\n')
    myFile.write(str(random.randrange(50000, 1000000, 10000)))
    myFile.write('\n')
    myFile.write(str(random.randint(1, 10)))
    myFile.write('\n')
    myFile.write("1402/")
    myFile.write(str(random.randint(1, 11)))
    myFile.write('/')
    myFile.write(str(random.randint(1, 30)))
    myFile.write("\n-----------------------\n")
    
    
    
    
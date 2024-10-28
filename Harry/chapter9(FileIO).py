'''string = "Uday is a genius"

f = open("FileIO.txt", "w")

f.write(string)
f.close()

f2 = open("FileIO.txt")

val = f2.read()
print(val)

f2.close()'''

#------With statement
'''
with open("FileIO.txt") as f:
    print(f.read())'''

#---------

'''with open("FileIO.txt") as f:
    r= f.read()

    val =r.find("also")
    print(val)
    print(r[73:77])'''

'''with open("FileIO.txt") as f:
    r= f.readline()
    while r != "":
        
        val= r.find("also")
        if val != -1:
            print(val)

        r = f.readline()'''

#---------HI-score
'''import random
def game():
    val = int(100* random.uniform(0,1))
    return val
score = game()
print(score)

with open("Harry/Hi-score.txt", "r") as f:
    text= int(f.read())
    print(text)

if score >= text:
    with open("Harry/Hi-score.txt","w") as k:
        k.write(str(score))'''

#-----------Tables

'''def table():
    string =[]

    for j in range(1,21):
        val =str(f"{j} x {i} = {i*j}")
        string.append(val)
    return string

for i in range(1,21):
    with open("Harry/FileIOTables/{i}Table.txt", "w") as f:
        f.write(str(table()))'''
#----Tables working
'''for i in range(1,21):
    file_path = f"Harry/FileIOTables/{i}Table.txt"

    for j in range(1,21):
        
        val =str(f"{i} x {j} = {i*j} \n")
        with open(file_path, "a") as f:
            f.write(val)'''

#---------

'''with open("FileIO.txt", "r") as f:
    val =f.read()
    print(val)

    new = val.replace("Kiran", "Uday")
    new2 = new.replace("l","a")

with open("FileIO.txt", "w") as k:
    k.write(new2)'''

#------------

'''with open("Harry/Hi-score.txt", "r") as f:
    data =f.read()
with open("Harry/Hi-score2.txt", "w") as k:
    k.write(data)'''

#-------------
'''
with open("Harry/Hi-score.txt", "r") as f:
    data =f.read()

with open("Harry/Hi-score2.txt", "r") as k:
    data2 =k.read()

if data == data2:
    print("same data")
else:
    print("different data")'''

#-------------Clear the file
'''nothing =""
with open("Harry/Hi-score2.txt", "w") as k:
    k.write(nothing)
'''























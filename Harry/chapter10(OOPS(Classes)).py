
'''class Employee:
    language = "Python"

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
    
uday = Employee("Uday", 100000, "C++")
print(uday.name, uday.salary, uday.language)

# Throws an error as no parameters are given
# panda = Employee()

'''

#------programmers

'''class Programmers:

    salary = 100000
    language1 = "Python"
    language2 = "Java"
    salary2 = 90000

uday = Programmers()
uday.name ="Uday"
print(uday.name, uday.salary, uday.language1)

panda = Programmers()
panda.name= "Panda"
print(panda.name, panda.salary2, panda.language2)'''

#---------square,cube,sqr

'''n = int(input("Enter the number"))
import math

class Maths:
    number = 4

    def square(self):
        print(n*n)

    def cube(self):
        print(self.number*self.number*self.number)
    
    @staticmethod
    def sqr():
        print(math.sqrt(n))

number = Maths()
number.square()
number.cube()
number.sqr()
'''

#----------Train

'''class Train:

    n=120

    def __init__(self, bookTicket, price, status):
        
    
        
        if bookTicket == True:
            if Train.n>0:
                Train.n = Train.n-1
                print("Ticket Booked")
    
                if status == True:
                    print(f"Remaining Seats = {Train.n}")
            
        if price == True:
            price = 1200
            print(price)

uday = Train(True,True, True)

kishore = Train(True,False, True)
'''






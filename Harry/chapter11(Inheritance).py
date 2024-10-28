'''class Employee:    #Base Class 

    company = "ITC"

    @staticmethod
    def salary():
        print(100000)

class Programmer(Employee):    #Derived class

    company = "ITC DevOps"

    @staticmethod
    def language():
        print("Python")


uday = Employee()
uday.salary()
print(uday.company)

kiran = Programmer()
print(kiran.company)
kiran.language()'''


#---------Super

'''class Employee:    #Base Class 
    def __init__(self):
        super().__init__()
        print("Employee Constructor")
    company = "ITC"

    @staticmethod
    def salary():
        print(100000)

class Coder:
    def __init__(self):
        super().__init__()
        print("Coder Constructor")

class Programmer(Employee, Coder):    #Derived class
    def __init__(self):
        super().__init__()
        print("Programmer Constructor")

    company = "ITC DevOps"

    @staticmethod
    def language():
        print("Python")

class Senior(Programmer):
    def __init__(self):
        super().__init__()
        print("Senior Constructor")
        

uday  = Senior()'''

#------------- @classmethod

'''class Employee:
    a= 1

    @classmethod     #This tag helps the function to use only class attributes
    def func(cls):   #use "cls" instead of "self" for readability
        print(f"The value of calss attribute is {cls.a}")

uday = Employee()
uday.a = 23
uday.func()'''

#-------- @property & @ setter

'''class Employee:

    @property    # Property is a getter, it gets the value of name attribute either in __init__ or object attribute
    def name(self):
        
        return self.ename.lower()
    
    @name.setter
    def name(self,value):
        self.ename = value
        

uday = Employee()
uday.name = "Sidagana Uday"
print(uday.name)
'''

'''class Employee:
    
    def __init__(self, name):
        self.ename = name

    @property    # Property is a getter, it gets the value of name attribute either in __init__ or object attribute
    def name(self):
        
        return self.ename.lower()
    
    @name.setter
    def name(self,value):
        self.ename = value
        

uday = Employee("Sidagana Uday")

print(uday.name)'''

#-------------

'''class Number:
    def __init__(self,n):
        self.n = n
    
    def __add__(self, num):
        return self.n + num.n
    
a = Number(1)
b= Number(2)
c= Number(4)

print(a + b)'''

#----------

'''class TwoD:

    x= 2
    y = 3

class ThreeD(TwoD):
    z=4

vector = ThreeD()
print(vector.x, vector.y,vector.z)'''

#-----------

'''class Animals:
    type1= "Mamals"
    type2= "Amphibious"
    type3= "Birds"
    type4= "Fish"

class Pets(Animals):

    place = "Home"

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow! Bow!")

puppy = Dog()
puppy.name = "Mogambo"
print(f"Hi, {puppy.name} is a pet and he come under {puppy.type1}. He is Cute and stays at {puppy.place}")'''

#------------

'''class Employee:

    def __init__(self,salary):
        self.salary = salary

    @property
    def salaryAfterIncrement(self):
        if self.salary >= 100000:
            return self.salary
        elif self.salary >=30000 and self.salary < 100000:
            return self.salary+ 10000
        else:
            return self.salary+ 20000
    

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        self.salary = value
        



uday = Employee(100000)
uday.name ="Uday"
print(uday.salaryAfterIncrement)'''

'''class Employee:

    def __init__(self,salary):
        self.nsalary = salary

    @property
    def salary(self):
        if self.nsalary >= 100000:
            return self.nsalary
        elif self.nsalary >=30000 and self.nsalary < 100000:
            return self.nsalary+ 10000
        else:
            return self.nsalary+ 20000
    

    @salary.setter
    def salaryAfterIncrement(self, value):
        self.nsalary = value
        



uday = Employee(80000)
uday.name ="Uday"
print(uday.salary)'''

#-------------

'''class Complex:

    def __init__(self, i):
        self.i = i

    def __add__(self,num):
        return self.i + num.i
    
    def __mul__(self, num):
        return self.i * num.i
    
number = Complex(2)
numbers = Complex(3)


print(number + numbers)'''


#--------------Vector

'''class TwoD:
    def __init__(self,i, j):
        self.i = i
        self.j =j

    def show(self):
        print(f"{self.i}i + {self.j}j")

class ThreeD(TwoD):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")

vector = TwoD(2,3)
threeDvector = ThreeD(2,3,4)
vector.show()
threeDvector.show()'''

#-------------Vector Complex dot and sum

'''class Complex:

    def __init__(self, r, i, dot):
        self.r = r
        self.i = i
        self.dot = dot

    def __add__(self, c2):
        return f"{self.r + c2.r} + {self.i + c2.i}i"
    
    def __mul__(self, c2):
        if self.dot == False:
            return f"Multiplication is : {(self.r*c2.r)-(self.i*c2.i)} + {(self.r*c2.i) + (c2.r*self.i)}i"     #ac-bd + (ad+bc)i
        else:
            return f"Dot is : {(self.r*c2.r)+ (self.i*c2.i)}"
    
    
    
numbers = Complex(3,5,True)  #True or False value of numbers defines the outcome rather than c2
c2 = Complex(2,1,True)

print(numbers + c2)
print(numbers * c2)'''


#-----------
        

from testing import myFunction

'''a = 10

def func():
    global a  #This changes the value of global a=10 to a=2
    a= 2
    print(a)

func()
print(a)'''

#---------Enumerate (Adds counter to an iterable and returns the value)

'''l=[11,22,33,44,55]

# index =0

# for i in l:
#     print(f"The item at index {index} is {i}")
#     index += 1
for index, i in enumerate(l):
    print(f"The item at index {index} is {i}")'''

#--------------Lists

'''numbers =[1,2,3,4,5]

# square =[]
# for i in numbers:
#     square.append(i*i)
square = [i*i for i in numbers]

print(square)
'''
#----------Multiple files and Error Handling
'''try:
        
    with(open("Harry/chapter1.py") as f1,
        open("Harry/chapter2.py") as f2,
        open("jaffa.py") as f3):
        
        f1.read()
        f2.read()
        f3.read() 

except FileNotFoundError as e:
    print(e)'''

#----------Enumerate

'''l =[1,2,3,4,5,6,7,8]

for index, i in enumerate(l):
    if index == 4 or index == 6 or index ==7:
        print(f"{index}, {i}") '''

#--------table

'''inp = int(input("Enter the number"))

# list = [1,2,3,4,5,6,7,8,9,10]

# table = [inp*i for i in list]
table = [inp*i for i in range(1,11)]

print(table)

# with open("AdvTable.txt", "w") as f:
#     f.write(str(table))
'''

#----------

'''a : int = int(input("a: "))
b: int = int(input("b: "))

try:
    print(a/b)

except ZeroDivisionError:
    print("Infinite")

print("Done")'''

#----------Map

'''l = [1,2,3,4,5]

square = lambda x: x*x

square_List = map(square, l)
print(list(square_List))'''


#------------Filter

'''l = [1,2,3,4,5,6]
def even(n):
        if (n % 2 == 0):
            return True
        
even_numbers = filter(even, l)
print(list(even_numbers))'''

#-------Reduce
'''from functools import reduce

l = [1,2,4,5]
def sum(a,b):
    return a+b

mul = lambda a,b: a*b

sum_list = reduce(sum,l)
mul_list = reduce(mul, l)

print(sum_list)
print(mul_list)'''

#-----------Format ex
'''name = input("Name: ")
marks= int(input("Marks: "))
phone_no = int(input("Phone.no: "))

print("Name of the student is {}, He got {} marks. For further details call him at {}".format(name,marks,phone_no))'''

#----------
'''from functools import reduce
l = [1,2,3,4,5,6]

def string(n):
    return str(n)

new = reduce(string, l)
print(new)'''

#--------Table

'''table = [str(2*i) for i in range(1,11)]

formatted = "\n".join(table)

print(formatted)'''

#----------
'''from functools import reduce
l =[1,2,5,10,25,20,3,6]

def div_five(n):
    if n%5==0:
        return True
    
five = filter(div_five, l)

print(list(five))
'''

#-------greatest
'''from functools import reduce
l =[1,35,4,23,90,76]

def greatest(a,b):
    if a>b:
        return a
    return b
    
final = reduce(greatest, l)
print(final)
'''

#---------







    


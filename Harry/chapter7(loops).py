'''i=0
while i<5:
    print("Uday")
    i +=1'''

#----------
'''
list = [23,45,2,90,76]
i=0
while i<len(list):
    print(list[i])
    i+=1'''

#-----------9 table

'''for i in range(0,100,9):
    print(i)'''

#-----------for and else togeather

'''list = [12,45,32,11,10]
sum =0
for i in list:
    print(i)
else:
    for i in list:
        sum += i
    print(f"sum is:{sum}")'''

#---------

'''for i in range(10):
    print(i)
    if(i==7):
        break #exit loop immediately'''

'''for i in range(20):
    
    if(i==7):
        continue #skip this iteration
    print(i)
'''
'''
for i in range(100):
    pass # to halt the loop'''
    
#----------Table

'''number = int(input())

for i in range(1,20):
    print(f"{number} x {i} = {number*i}") '''

#-------------

'''list1 = ["Uday", "Sidagana", "Saloni", "Sam", "Kiran", "Bahubali"]
starts = input("The letter")

# for i in list1:
#     if i.startswith("S"):
#         print(f"Hi {i}")

# for i in list1:

#     if (i[0].lower()== starts.lower()):
#         print(f"HI {i}")

for i in list1:

    for j in i:
        if (j.lower() == starts.lower()):
            print(f"HI {i}")'''

#-----------
'''number = int(input("The number"))

i = 0
while i<=20:
    print(f"{number} x {i} = {number*i}")
    i +=1'''

#--------- Prime

'''for i in range(2,20):
    if (i==2 or i==3 or i==5 or i==7):
        print(i)
    else:
    
        if(i%2 == 0 or i%3 == 0 or i%4==0 or i%5==0 or i%6==0 or i%7==0 or i%9 == 0 ):
            pass
        
        else:
            print(i)
'''
    
#-------sum of n natural

'''n = int(input())
sum =0
i=1
while(i<n+1):
    sum += i
    i += 1
print(sum)
'''

#--------Factorial
'''n = int(input())
val =1
for i in range(1,n+1):
    val = val*i
print(val)'''

# #-------   *
#          *   *
#       *    *    *

'''n = int(input())

for i in range(0, n+1):

    space = int(n-i)
    #print(space)
    print(f"{(space) * '  '}{i*' *  '}")

    #print(f"{int(((n+1)-i)/2)*' '}{i*'*'}")
    
    # print(f"{' '* (int(((n+1)/2) - i))}{i*'*'}")'''

#--------------
'''n = int(input())
for i in range(1,n+3, 2):
    space = ((n+2)-i)
    print(f"{space * ' '}{i*'* '}")'''

#-------------- for printing square, man i really put my head for this logic
'''import math
n = int(input())


for i in range(1,n+1):
    space= (n+(int(((n+1)/2)-2)))
    if (i==1 or i ==n):
        print(n*'*  ') # For the first line and last line

    elif(n%2==0):                #For even number of n
        print(f"*{space*'  '}*") 

    else:                        #For odd n
        init =5

        for j in range(3, n+1,2):
            if j>3:               #logic: 3-->5, 5-->11, 7-->17, 9-->23 ....
                
                init += 6
        space= (init)
        
        print(f"*{(space)*' '}*")'''

#------------
'''List=[1,2,3,4,5,6,7,8,9,10]
number = int(input())


for i in List:
    val = List[-i]
    print(f"{number} x {val} = {number*val}")
'''
#------------ Code with Harry analogy
'''n = int(input())
for i in range(1,n+n,2):
    space = (n+n)-i
    print(f"{space*' '}{i*' *'}")'''
'''
n = int(input())
for i in range(1, n+1):
    print((n-i)*" ", end="")
    print((2*i-1)*'*', end="")
    print("")'''

#------------

'''n = int(input())
for i in range(1, n+1):
    if(i==1 or i==n):
        print("*"*n)
    else:
        print(f"*{' '*(n-2)}*")
'''

#------------
'''n = int(input("Which table:"))
upto = int(input("Upto what number you want your table to be printed?"))
upto_per = (upto/10)-1
for i in range(1,upto+1):
    print(f"{n} x {11+(upto_per*10)-i} = {n*(11+(upto_per*10)-i)}")
'''





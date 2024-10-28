#create modules on PYPI for the complex logic you thought of
#---------
'''def factorial(n):
    if n ==0 or n==1:
        return 1

    return n*factorial(n-1)
n = int(input())
print(factorial(n))'''

#--------greatest


'''def greatest():
    list1 = [23,4,3,1,7,8,12,90,45]
    great = 0
    list2 =[]
    for i in range(int((len(list1)/2))):
        val = list1[i]
        val2 = list1[-i]
        
        if val>= val2:
            great = val
            list2.append(great)
        else:
            great = val2
            list2.append(great)

    list1 = list(set(list2))

    if list1[0] >= list1[1]:
        greatest_number = list1[0]

    else:
        greatest_number = list1[1]

    return greatest_number
 


print(greatest())'''

#----------------Celcius to Farenheit
'''inp = int(input("Enter Your Temperature: "))
choice = int(input("What is the format of temperature you entered? \n '1' for Celcius '2' for Farenheit"))
def To_celcius():
    celcius = (inp-32)*(5/9)
    return celcius

def To_farenheit():
    farenheit = inp*(9/5)+32
    return farenheit

if choice ==1:
    print(To_farenheit())

elif choice == 2:
    print(To_celcius())

else:
    print("Invalid Temperature or Format")'''

#----------------sum of n natural
'''
n = int(input())

def sum(n):
    if n ==0:
        return 0
    return n+(sum(n-1))

print(sum(n))'''

#--------------pattern

'''def star():

    n = int(input())
    for i in range(n+1):
        print((n-i)*"*")
star()
'''

#------- cm to inches

'''def cm_to_inches(cms):
    inches = cms*2.54
    return inches
print(cm_to_inches(100))'''

#-----------remove and strip

lists = ["Uday", " Sidagana", " Kiran "]

'''def remove_and_strip():
    list2 =[]
    lists.remove("Uday")

    for i in lists:
        new = i.strip()
        list2.append(new)
    return list2

print(remove_and_strip())'''

#------------table

'''def table(n):
    for i in range(1,21):
        print(f"{n} x {i} = {n*i}")

n = int(input())

table(n)'''

#------------



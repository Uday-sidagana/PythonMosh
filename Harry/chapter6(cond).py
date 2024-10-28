# Complex code to find greatest, damn i feel like a god
'''lists = [12,4,3,1,6,5,9,2]

for j in range(len(lists)):
    list2 =[]

    for i in range(len(lists)):
        val1 = lists[i]
        val2 = lists[-i]
    
        if val1>=val2:
           list2.append(val1) 
        else:
            list2.append(val2)
    

    lists = list(set(list2))
 
   #This part is further done because our logic of using lists[i] and -i will comapre 0 index
   # twice and the next index also twice because there's only one left.(no matter how many iterations we use we get the same [a,b]) 
if lists[0]>=lists[1]:
    print(lists[0])
else:
    print(lists[1])'''

#---------------2nd way to get the greatest among the list

'''list1 = [1,5,10,4,6,2]

list1.sort()
print(list1[-1])'''

#----------Marks


'''marks =[]
subject= int(input("What is the value of each subject:"))

for j in range(3):
    mark = input(f"Subject{j}")
    marks.append(mark)
total =0
for i in marks:
    total = total +int(i)
    

tot_per = (total*100)/(subject*3)
    
failed = False
for k in marks:
    per = (int(k)/subject)*100
    print(per)

    if per>32 and tot_per>40:
        print("Pass")
    else:
        failed= per
        print("Fail")

if failed:
    print("Failed")
else:
    print("Pass")'''


#-----------

'''message = "My name is Uday Sidagana"


#The spam keywords are in val and val2
val= message.find("Free")
val2 = message.find("Money")

if val>0 or val2>0:
    print("Spam")
else:
    print("Not Spam")
# can also use if (val in message or val2 in message)
'''

#-------------

'''username = input()
if len(username)>=10:
    print("Pass")
else:
    print("Short")
'''

#--------

'''lists = ["Uday",23,"Sidagana"]

val = lists.count("Uday")
print(val)

if val>0:
    print("Exists")
else:
    print("Not")'''

#----------

post = "Uday sidagana is fucking sexy"
name = "Kiran"
if(name.lower() in post.lower()):
    print("This post is talking about uday")

else:
    print("Not talking about Uday")






        



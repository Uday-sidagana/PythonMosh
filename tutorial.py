"""name= input("What's Your name? ")
fav_color= input("What's your favourite color ")
print(name+" loves "+fav_color)"""

'''weight = int(input("Weight: "))
kilograms = weight*1.2
print(kilograms)'''

'''Default_weight= input("(L) for lbs or (K) for Kgs ")

weight= input("Enter weight")
x= Default_weight.upper()




if x == "K":
    print(f'Your weight in pounds is: {int(weight)*2}')

if x == "L":
    print(f'Ypur weight in Kilograms is {int(weight)*0.5}')

else:
    print("Enter a valid weighht")'''

'''sec_num = 9

i =1
while i <4:
    
    num = input("Guess: ")
    x= int(num)
    
    if x == sec_num:
        print("Correct")
    i = i+1'''

"""command = ""
status = ""

while True:
    command = input("? ").lower()
    
    if command == "start":
        if status == "started":
            print("Engine is already on.")
        else:
            print("Car started!")
            status = "started"
    
    elif command == "stop":
        if status == "stopped":
            print("Engine is already off.")
        else:
            print("Car stopped.")
            status = "stopped"
    
    elif command == "quit":
        break
    
    else:
        print("Invalid input, please try 'start', 'stop', or 'quit'.")"""

"""for item in range(1,10,2): #(1:Start, 10: end, 2: step(skip))
   print(item)"""

"""prices = [10, 20, 30]
choice = ""
cart = []
value = 0

while True:
    choice = input("Choose 'one', 'two', 'three', or 'done': ").lower()
    
    if choice == "one":
        cart.append(prices[0])
    elif choice == "two":
        cart.append(prices[1])
    elif choice == "three":
        cart.append(prices[2])
    elif choice == "done":
        
        for item in cart:
            value += item
        print(f"Total value of items in the cart: {value}")
        break  # Exit the loop after calculating the total
    else:
        print("Choose wisely. Options are 'one', 'two', 'three', or 'done'.")"""


"""
phone = input("Phone no: ")
print(phone)
list = []
value =""
for j in phone:
    if j == "1":
        value = "One"
    if j == "2":
        value = "Two"
    if j == "3":
        value = "Three"
    list.append(value)
print(list)
    """

 






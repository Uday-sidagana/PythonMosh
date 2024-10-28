'''marks = {"uday": 300, "Sidagana":1000}

marks2 = {1:"Kiran", 2:"Amoeba"}

print(marks["uday"])
print(marks2[2])'''

#--------

'''keys =['a','b','c']

new_dict = dict.fromkeys(keys, 0)

print(new_dict)

new_dict.pop('a')
print(new_dict)'''

#----------

'''dictionary = {"aaja":"Come", "baith":"Sit", "Sunle":"listen"}

search = input("Search:")

print(dictionary.get(search))'''

#--------

'''numbers = set()

for i in range(8):

    inp = int(input())
    numbers.add(inp)

print(numbers)'''

#------------
'''
set1 ={18, "18", 21,45}
print(set1)'''

#------------

dictionary= {}



for i in range(4):
    names = input("name")
    lang = input("value")
    
    dictionary.update({names:lang})

print(dictionary)
    




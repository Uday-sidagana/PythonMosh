# #_------ List Comphrension
# x=1
# y=2
# z=3
# list =[]
# new_list=[]

# for i in range(3):
#     list.insert(i, x)

#     for j in range(1):
#         if list[i]!=None:
#             list.insert(i+1,y)
#             # print(list)
            
#             for k in range(1):
#                 if list[i]!=None and list[j]!=None:
#                     list.insert(3-(i+j),z)
#                     # new_list.append(list)
#                     # print(new_list)
                    
#     # list.clear()
# print(list)

# Define the range for x, y, z
# Define the values for x, y, z
values = [1, 2, 3,0]

# # Generate all combinations without libraries
# for x in values:
#     for y in values:
#         for z in values:
#             if x != y and y != z and x != z:  # Ensure all values are different
#                 print((x, y, z))

# lis = [1,2,3]
# value =[]
# new_list=[]
# n=3
    
# for i in lis:
    
#     for j in lis:
       
#         for k in lis:
#             new_list=[i,j,k]
#             if i+j+k != n:
#                 value.append(new_list)


# print(value)

'''x = int(input())
y = int(input())
z = int(input())
n = int(input())

lis = [x,y,z,0]
value =[]
new_list=[]

for i in lis:
    
    for j in lis:
    
        for k in lis:
            new_list=[i,j,k]
            if i+j+k != n :
                if new_list not in value:

                    value.append(new_list)

print(value)
'''

# n = int(input())
# arr = map(int, input().split())
# arr_list= list(arr)
# print(arr_list)
# lis=[]

# for i in range(int(n/2)):
#     if arr_list[i] > arr_list[-i]:
#         lis.append(arr_list[i])
#     else:
#         lis.append(arr_list[-i])
#     print(lis)

# print(lis)

'''n = int(input())
arr = map(int, input().split())
arr_list =list(arr)

arr_list.sort()
for i in range(1, len(arr_list)):
    if arr_list[-i] != arr_list[-i-1]:
        print(arr_list[-i-1])
        break'''
# final_list =[]
# second_lowest_list =[]
# second_lowest_list_sort =[]

# for i in range(int(input())):
#         name = input()
#         score = float(input())
#         lis = [name,score]
#         final_list.append(lis)

# lowest= None
# second_lowest= None       
    
# for i in final_list:
        
#     grade = i[1]
#     if lowest == None or grade <=lowest:
#             second_lowest = lowest
#             lowest = grade
#     elif second_lowest ==None or grade<=second_lowest:
#             second_lowest = grade

# for j in final_list:
#        if j[1] == second_lowest:
#               second_lowest_list.append(j[0])
              

# second_lowest_list_sorted = sorted(second_lowest_list, key=lambda x: x.lower())

# for m in second_lowest_list_sorted:
#        print(m)

'''if __name__ == '__main__':
    alist = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        alist.append([name, score])
second_highest = sorted(set([score for name, score in alist]))[1]
print('\n'.join(sorted([name for name, score in alist if score == second_highest])))'''

       
       


            
       

# print(second_lowest)

                
        
        


    


            
     







    
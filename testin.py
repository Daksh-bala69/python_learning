# tup=(1,3,4,4)
# li =[]
# li.append(tup[0])
# li.append(tup[1])
# print(type(li))
# print(li)
# info ={
#     "name": "daksh",
#     "age":17,
#     "college":"dtu",
#     "salary":0,
#     "score" : {
#         "phy": 89,
#         "chem":84,
#         "math":89
#     },
#     "arms": 2
# }
# info["legs"]=2
# print (info)
# print (info["score"]["phy"])
# print(info.keys()) 
# print(len(info))
# print(list(info.items()))
# collection = set()
# #collection1={}
# print (type(collection))
# #print (type(collection1))
# collection.add(945)
# collection.add("hello")
# collection.add(True)
# print (collection)
# set1= {"python","java","c++","python","javascript"}
# set2={"java","python","java","c++","c"}
# print(len(set1.union(set2)))
# subjects= {}
# math_marks=input("Enter your marks in maths:")
# subjects.update("Maths":math_marks)
# hindi_marks=input("Enter your marks in hindi:")
# subjects.update("Hindi":hindi_marks)
# frech_marks=input("Enter your marks in french:")
# subjects.update("French":french_marks)
# print(subjects)
# li =[1,4,9,16,25,36,49,64,81,100]
# num=int(input("Enter the number you want to serch:"))
# idx=0
# for el in li:
#     if el==num:
#         print("The index of the element you want to find is:",idx)
#         break
#     idx+=1    
# for i in range(1,5,2):
#     print (i)
# num=int (input("Enter the number:"))
# for i in range(num,num*10+1,num):
#     print(i)
# i=1
# summ=0
# n=int(input("Enter the number:"))
# while i<n:
#     summ=summ+i
#     i+=1
# # print (summ)
# factorial=1
# n=int(input("Enter the nummber:"))
# for i in range(1,n+1):
# #     factorial*=i
# # print(factorial)
# def num_identifier(num):
#     if num%2==0:
#         print("EVEN")
#     else:
#         print("ODD")

# num_identifier(5)
# def sum_n(n):
#     if(n==0):
#         return 0
#     return n+sum_n(n-1)

# summ=sum_n(11)
# print(summ)

# import final as np
for i in range(10):
    print (i)
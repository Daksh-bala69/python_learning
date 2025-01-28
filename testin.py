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
collection = set()
#collection1={}
print (type(collection))
#print (type(collection1))
collection.add(945)
collection.add("hello")
collection.add(True)
print (collection)
set1= {"python","java","c++","python","javascript"}
set2={"java","python","java","c++","c"}
print(len(set1.union(set2)))
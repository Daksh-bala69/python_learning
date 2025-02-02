import numpy as np
import cv2
import math

#for front angle
from ultralytics import YOLO
model=YOLO("C:\\Users\\BEAST SSJ3\\Downloads\\best.pt")
results=model.predict(r"C:\Users\BEAST SSJ3\Downloads\UAS_DTU_Round_2_Task_data\UAS_DTU_Round_2_Task_data\5\images_close_img_14_23.jpg",save=True)

for result in results:
    print(result.boxes.numpy)

results1=model.predict(r"C:\Users\BEAST SSJ3\Downloads\UAS_DTU_Round_2_Task_data\UAS_DTU_Round_2_Task_data\5\images_close_img_14_23_back.jpg",save=True)

for result1 in results1:
    print(result1.boxes.numpy)

def bubbleSort(arr): 
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



#count for all the objects(front)
count_for1_front=0
count_for2_front=0
count_for3_front=0

#count for all the objects(back)
count_for1_back=0
count_for2_back=0
count_for3_back=0

#list of indexes of occurances of each object in the cls array(front)
idx_for_1_front=[]
idx_for_2_front=[]
idx_for_3_front_sortedInX=[]

#list of indexes of occurances of each object in the cls array(back)
idx_for_1_back=[]
idx_for_2_back=[]
idx_for_3_back_sortedInX=[]

#list of indexes of occurances of each object in the cls array but this time image specific
idx_for_1_inside_plant1_front=[]
idx_for_2_inside_plant1_front=[]
idx_for_1_inside_plant2_front=[]
idx_for_2_inside_plant2_front=[]
idx_for_1_inside_plant3_front=[]
idx_for_2_inside_plant3_front=[]

#list of indexes of occurances of each object in the cls array but this time image specific
idx_for_1_inside_plant1_back=[]
idx_for_2_inside_plant1_back=[]
idx_for_1_inside_plant2_back=[]
idx_for_2_inside_plant2_back=[]
idx_for_1_inside_plant3_back=[]
idx_for_2_inside_plant3_back=[]

#list of temporary x values for each object
x_for_3=[]
x_for_2=[]
x_for_1=[]

#list of temporary y valuas for each object
y_for_3=[]
y_for_2=[]
y_for_1=[]

#list of distance(in x) from the centre of the '3' class object to the centre of the fruits (2,3) in a image specific manner(front)
xdistance_for_1_from_plant1_front=[]
xdistance_for_1_from_plant2_front=[]
xdistance_for_1_from_plant3_front=[]
xdistance_for_2_from_plant1_front=[]
xdistance_for_2_from_plant2_front=[]
xdistance_for_2_from_plant3_front=[]

#list of distance(in x) from the centre of the '3' class object to the centre of the fruits (2,3) in a image specific manner(back)
xdistance_for_1_from_plant1_back=[]
xdistance_for_1_from_plant2_back=[]
xdistance_for_1_from_plant3_back=[]
xdistance_for_2_from_plant1_back=[]
xdistance_for_2_from_plant2_back=[]
xdistance_for_2_from_plant3_back=[]

#list of distance(in y) from the centre of the '3' class object to the centre of the fruits (2,3) in a image specific manner(front)
ydistance_for_1_from_plant1_front=[]
ydistance_for_1_from_plant2_front=[]
ydistance_for_1_from_plant3_front=[]
ydistance_for_2_from_plant1_front=[]
ydistance_for_2_from_plant2_front=[]
ydistance_for_2_from_plant3_front=[]

#list of distance(in y) from the centre of the '3' class object to the centre of the fruits (2,3) in a image specific manner(back)
ydistance_for_1_from_plant1_back=[]
ydistance_for_1_from_plant2_back=[]
ydistance_for_1_from_plant3_back=[]
ydistance_for_2_from_plant1_back=[]
ydistance_for_2_from_plant2_back=[]
ydistance_for_2_from_plant3_back=[]

#double counted elements which are to be substracted
to_substract_1_from_plant1=0
to_substract_2_from_plant1=0
to_substract_1_from_plant2=0
to_substract_2_from_plant2=0
to_substract_1_from_plant3=0
to_substract_2_from_plant3=0

#array of the classes of each object detected(front)
arr=result.boxes.cls.cpu().numpy()

#array of the classes of each object detected(back)
arr1=result1.boxes.cls.cpu().numpy()

#array of the xyxy format coordinates of each object(front)
coor_xy=result.boxes.xyxy.cpu().numpy()

#array of the xyxy format coordinates of each object(back)
coor_xy1=result1.boxes.xyxy.cpu().numpy()

#array of the xywh format coordinates of each object(front)
coor_center=result.boxes.xywh.cpu().numpy()

#array of the xywh format coordinates of each object(back)
coor_center1=result1.boxes.xywh.cpu().numpy()

#loop to find the index and the initial count of the obects according to their classes (including doubly counted elemts)(front)
for i in range(arr.size):
    if(arr[i]==1):
        count_for1_front+=1
        idx_for_1_front.append(i)

    if(arr[i]==2):
        count_for2_front+=1
        idx_for_2_front.append(i)

    if(arr[i]==3):
        count_for3_front+=1
        idx_for_3_front_sortedInX.append(i)

for i in range(len(idx_for_3_front_sortedInX)):
    for j in range(len(idx_for_3_front_sortedInX)-i-1):
        if(coor_center[idx_for_3_front_sortedInX[j]][0]>coor_center[idx_for_3_front_sortedInX[j+1]][0]):
            idx_for_3_front_sortedInX[j],idx_for_3_front_sortedInX[j+1]=idx_for_3_front_sortedInX[j+1],idx_for_3_front_sortedInX[j]


#loop to find the index and the initial count of the obects according to their classes (including doubly counted elemts)(back)
for i in range(arr1.size):
    if(arr1[i]==1):
        count_for1_back+=1
        idx_for_1_back.append(i)

    if(arr1[i]==2):
        count_for2_back+=1
        idx_for_2_back.append(i)

    if(arr1[i]==3):
        count_for3_back+=1
        idx_for_3_back_sortedInX.append(i)

for i in range(len(idx_for_3_back_sortedInX)):
    for j in range(len(idx_for_3_back_sortedInX)-i-1):
        if(coor_center1[idx_for_3_back_sortedInX[j]][0]>coor_center1[idx_for_3_back_sortedInX[j+1]][0]):
            idx_for_3_back_sortedInX[j],idx_for_3_back_sortedInX[j+1]=idx_for_3_back_sortedInX[j+1],idx_for_3_back_sortedInX[j]

print(idx_for_3_front_sortedInX)
print(idx_for_3_back_sortedInX)
#loop to fint he index of each ojbets but specific to the image/angle by checking which objects lie inside the class '3'objects(front)
for i in range(int(len(idx_for_3_front_sortedInX))):
    if(i==0):
        for j in range(int(len(idx_for_1_front))):
            if(coor_xy[idx_for_3_front_sortedInX[i]][0]<=coor_xy[idx_for_1_front[j]][0] and coor_xy[idx_for_3_front_sortedInX[i]][1]<=coor_xy[idx_for_1_front[j]][1] and coor_xy[idx_for_3_front_sortedInX[i]][2]>=coor_xy[idx_for_1_front[j]][2] and coor_xy[idx_for_3_front_sortedInX[i]][3]>=coor_xy[idx_for_1_front[j]][3]):
                idx_for_1_inside_plant1_front.append(idx_for_1_front[j])

        for j in range(int(len(idx_for_2_front))):
            if(coor_xy[idx_for_3_front_sortedInX[i]][0]<=coor_xy[idx_for_2_front[j]][0] and coor_xy[idx_for_3_front_sortedInX[i]][1]<=coor_xy[idx_for_2_front[j]][1] and coor_xy[idx_for_3_front_sortedInX[i]][2]>=coor_xy[idx_for_2_front[j]][2] and coor_xy[idx_for_3_front_sortedInX[i]][3]>=coor_xy[idx_for_2_front[j]][3]):
                idx_for_2_inside_plant1_front.append(idx_for_2_front[j])

    if(i==1):
        for j in range(int(len(idx_for_1_front))):
            if(coor_xy[idx_for_3_front_sortedInX[i]][0]<=coor_xy[idx_for_1_front[j]][0] and coor_xy[idx_for_3_front_sortedInX[i]][1]<=coor_xy[idx_for_1_front[j]][1] and coor_xy[idx_for_3_front_sortedInX[i]][2]>=coor_xy[idx_for_1_front[j]][2] and coor_xy[idx_for_3_front_sortedInX[i]][3]>=coor_xy[idx_for_1_front[j]][3]):
                idx_for_1_inside_plant2_front.append(idx_for_1_front[j])

        for j in range(int(len(idx_for_2_front))):
            if(coor_xy[idx_for_3_front_sortedInX[i]][0]<=coor_xy[idx_for_2_front[j]][0] and coor_xy[idx_for_3_front_sortedInX[i]][1]<=coor_xy[idx_for_2_front[j]][1] and coor_xy[idx_for_3_front_sortedInX[i]][2]>=coor_xy[idx_for_2_front[j]][2] and coor_xy[idx_for_3_front_sortedInX[i]][3]>=coor_xy[idx_for_2_front[j]][3]):
                idx_for_2_inside_plant2_front.append(idx_for_2_front[j])

    if(i==2):
        for j in range(int(len(idx_for_1_front))):
            if(coor_xy[idx_for_3_front_sortedInX[i]][0]<=coor_xy[idx_for_1_front[j]][0] and coor_xy[idx_for_3_front_sortedInX[i]][1]<=coor_xy[idx_for_1_front[j]][1] and coor_xy[idx_for_3_front_sortedInX[i]][2]>=coor_xy[idx_for_1_front[j]][2] and coor_xy[idx_for_3_front_sortedInX[i]][3]>=coor_xy[idx_for_1_front[j]][3]):
                idx_for_1_inside_plant3_front.append(idx_for_1_front[j])

        for j in range(int(len(idx_for_2_front))):
            if(coor_xy[idx_for_3_front_sortedInX[i]][0]<=coor_xy[idx_for_2_front[j]][0] and coor_xy[idx_for_3_front_sortedInX[i]][1]<=coor_xy[idx_for_2_front[j]][1] and coor_xy[idx_for_3_front_sortedInX[i]][2]>=coor_xy[idx_for_2_front[j]][2] and coor_xy[idx_for_3_front_sortedInX[i]][3]>=coor_xy[idx_for_2_front[j]][3]):
                idx_for_2_inside_plant3_front.append(idx_for_2_front[j])


#loop to fint he index of each ojbets but specific to the image/angle by checking which objects lie inside the class '3'objects(back)
for i in range(int(len(idx_for_3_back_sortedInX))):
    if(i==0):
        for j in range(int(len(idx_for_1_back))):
            if(coor_xy1[idx_for_3_back_sortedInX[i]][0]<=coor_xy1[idx_for_1_back[j]][0] and coor_xy1[idx_for_3_back_sortedInX[i]][1]<=coor_xy1[idx_for_1_back[j]][1] and coor_xy1[idx_for_3_back_sortedInX[i]][2]>=coor_xy1[idx_for_1_back[j]][2] and coor_xy1[idx_for_3_back_sortedInX[i]][3]>=coor_xy1[idx_for_1_back[j]][3]):
                idx_for_1_inside_plant1_back.append(idx_for_1_back[j])

        for j in range(int(len(idx_for_2_back))):
            if(coor_xy1[idx_for_3_back_sortedInX[i]][0]<=coor_xy1[idx_for_2_back[j]][0] and coor_xy1[idx_for_3_back_sortedInX[i]][1]<=coor_xy1[idx_for_2_back[j]][1] and coor_xy1[idx_for_3_back_sortedInX[i]][2]>=coor_xy1[idx_for_2_back[j]][2] and coor_xy1[idx_for_3_back_sortedInX[i]][3]>=coor_xy1[idx_for_2_back[j]][3]):
                idx_for_2_inside_plant1_back.append(idx_for_2_back[j])

    if(i==1):
        for j in range(int(len(idx_for_1_back))):
            if(coor_xy1[idx_for_3_back_sortedInX[i]][0]<=coor_xy1[idx_for_1_back[j]][0] and coor_xy1[idx_for_3_back_sortedInX[i]][1]<=coor_xy1[idx_for_1_back[j]][1] and coor_xy1[idx_for_3_back_sortedInX[i]][2]>=coor_xy1[idx_for_1_back[j]][2] and coor_xy1[idx_for_3_back_sortedInX[i]][3]>=coor_xy1[idx_for_1_back[j]][3]):
                idx_for_1_inside_plant2_back.append(idx_for_1_back[j])

        for j in range(int(len(idx_for_2_back))):
            if(coor_xy1[idx_for_3_back_sortedInX[i]][0]<=coor_xy1[idx_for_2_back[j]][0] and coor_xy1[idx_for_3_back_sortedInX[i]][1]<=coor_xy1[idx_for_2_back[j]][1] and coor_xy1[idx_for_3_back_sortedInX[i]][2]>=coor_xy1[idx_for_2_back[j]][2] and coor_xy1[idx_for_3_back_sortedInX[i]][3]>=coor_xy1[idx_for_2_back[j]][3]):
                idx_for_2_inside_plant2_back.append(idx_for_2_back[j])

    if(i==2):
        for j in range(int(len(idx_for_1_back))):
            if(coor_xy1[idx_for_3_back_sortedInX[i]][0]<=coor_xy1[idx_for_1_back[j]][0] and coor_xy1[idx_for_3_back_sortedInX[i]][1]<=coor_xy1[idx_for_1_back[j]][1] and coor_xy1[idx_for_3_back_sortedInX[i]][2]>=coor_xy1[idx_for_1_back[j]][2] and coor_xy1[idx_for_3_back_sortedInX[i]][3]>=coor_xy1[idx_for_1_back[j]][3]):
                idx_for_1_inside_plant3_back.append(idx_for_1_back[j])

        for j in range(int(len(idx_for_2_back))):
            if(coor_xy1[idx_for_3_back_sortedInX[i]][0]<=coor_xy1[idx_for_2_back[j]][0] and coor_xy1[idx_for_3_back_sortedInX[i]][1]<=coor_xy1[idx_for_2_back[j]][1] and coor_xy1[idx_for_3_back_sortedInX[i]][2]>=coor_xy1[idx_for_2_back[j]][2] and coor_xy1[idx_for_3_back_sortedInX[i]][3]>=coor_xy1[idx_for_2_back[j]][3]):
                idx_for_2_inside_plant3_back.append(idx_for_2_back[j])


print("1 inside plant1(front):",idx_for_1_inside_plant1_front)
print("1 inside plant2(front):",idx_for_1_inside_plant2_front)
print("1 inside plant3(front):",idx_for_1_inside_plant3_front)
print("2 inside plant1(front):",idx_for_2_inside_plant1_front)
print("2 inside plant2(front):",idx_for_2_inside_plant2_front)
print("2 inside plant3(front):",idx_for_2_inside_plant3_front)
print("1 inside plant1(back):",idx_for_1_inside_plant1_back)
print("1 inside plant2(back):",idx_for_1_inside_plant2_back)
print("1 inside plant3(back):",idx_for_1_inside_plant3_back)
print("2 inside plant1(back):",idx_for_2_inside_plant1_back)
print("2 inside plant2(back):",idx_for_2_inside_plant2_back)
print("2 inside plant3(back):",idx_for_2_inside_plant3_back)


#this is for the distance for the objects in classes '1' and '2' for the plants(front angle)(in x)
for i in range(int(len(idx_for_3_front_sortedInX))):
    x_for_3.append(int(coor_center[idx_for_3_front_sortedInX[i]][0]))
    if(i==0):
        for j in range(len(idx_for_1_inside_plant1_front)):
            x_for_1.append(int(coor_center[idx_for_1_inside_plant1_front[j]][0]))
            xdistance_for_1_from_plant1_front.append(int(math.dist(x_for_3,x_for_1)))
            x_for_1.clear()
        for j in range(len(idx_for_2_inside_plant1_front)):
            x_for_2.append(int(coor_center[idx_for_2_inside_plant1_front[j]][0]))
            xdistance_for_2_from_plant1_front.append(int(math.dist(x_for_3,x_for_2)))
            x_for_2.clear()
        x_for_3.clear()

    if(i==1):
        for j in range(len(idx_for_1_inside_plant2_front)):
            x_for_1.append(int(coor_center[idx_for_1_inside_plant2_front[j]][0]))
            xdistance_for_1_from_plant2_front.append(int(math.dist(x_for_3,x_for_1)))
            x_for_1.clear()
        for j in range(len(idx_for_2_inside_plant2_front)):
            x_for_2.append(int(coor_center[idx_for_2_inside_plant2_front[j]][0]))
            xdistance_for_2_from_plant2_front.append(int(math.dist(x_for_3,x_for_2)))
            x_for_2.clear()
        x_for_3.clear()

    if(i==2):
        for j in range(len(idx_for_1_inside_plant3_front)):
            x_for_1.append(int(coor_center[idx_for_1_inside_plant3_front[j]][0]))
            xdistance_for_1_from_plant3_front.append(int(math.dist(x_for_3,x_for_1)))
            x_for_1.clear()
        for j in range(len(idx_for_2_inside_plant3_front)):
            x_for_2.append(int(coor_center[idx_for_2_inside_plant3_front[j]][0]))
            xdistance_for_2_from_plant3_front.append(int(math.dist(x_for_3,x_for_2)))
            x_for_2.clear()
        x_for_3.clear()


#this is for the distance for the objects in classes '1' and '2' for the plants(back angle)(in x)
for i in range(int(len(idx_for_3_back_sortedInX))):
    x_for_3.append(int(coor_center1[idx_for_3_back_sortedInX[i]][0]))
    if(i==0):
        for j in range(len(idx_for_1_inside_plant1_back)):
            x_for_1.append(int(coor_center1[idx_for_1_inside_plant1_back[j]][0]))
            xdistance_for_1_from_plant1_back.append(int(math.dist(x_for_3,x_for_1)))
            x_for_1.clear()
        for j in range(len(idx_for_2_inside_plant1_back)):
            x_for_2.append(int(coor_center1[idx_for_2_inside_plant1_back[j]][0]))
            xdistance_for_2_from_plant1_back.append(int(math.dist(x_for_3,x_for_2)))
            x_for_2.clear()
        x_for_3.clear()

    if(i==1):
        for j in range(len(idx_for_1_inside_plant2_back)):
            x_for_1.append(int(coor_center1[idx_for_1_inside_plant2_back[j]][0]))
            xdistance_for_1_from_plant2_back.append(int(math.dist(x_for_3,x_for_1)))
            x_for_1.clear()
        for j in range(len(idx_for_2_inside_plant2_back)):
            x_for_2.append(int(coor_center1[idx_for_2_inside_plant2_back[j]][0]))
            xdistance_for_2_from_plant2_back.append(int(math.dist(x_for_3,x_for_2)))
            x_for_2.clear()
        x_for_3.clear()

    if(i==2):
        for j in range(len(idx_for_1_inside_plant3_back)):
            x_for_1.append(int(coor_center1[idx_for_1_inside_plant3_back[j]][0]))
            xdistance_for_1_from_plant3_back.append(int(math.dist(x_for_3,x_for_1)))
            x_for_1.clear()
        for j in range(len(idx_for_2_inside_plant3_back)):
            x_for_2.append(int(coor_center1[idx_for_2_inside_plant3_back[j]][0]))
            xdistance_for_2_from_plant3_back.append(int(math.dist(x_for_3,x_for_2)))
            x_for_2.clear()
        x_for_3.clear()




print("Distance(in x) from plant1(front) for fruit type '1':",xdistance_for_1_from_plant1_front)
print("Distance(in x) from plant1(front) for fruit type '2':",xdistance_for_2_from_plant1_front)
print("Distance(in x) from plant2(front) for fruit type '1':",xdistance_for_1_from_plant2_front)
print("Distance(in x) from plant2(front) for fruit type '2':",xdistance_for_2_from_plant2_front)
print("Distance(in x) from plant3(front) for fruit type '1':",xdistance_for_1_from_plant3_front)
print("Distance(in x) from plant3(front) for fruit type '2':",xdistance_for_2_from_plant3_front)
print("Distance(in x) from plant1(back) for fruit type '1':",xdistance_for_1_from_plant1_back)
print("Distance(in x) from plant1(back) for fruit type '2':",xdistance_for_2_from_plant1_back)
print("Distance(in x) from plant2(back) for fruit type '1':",xdistance_for_1_from_plant2_back)
print("Distance(in x) from plant2(back) for fruit type '2':",xdistance_for_2_from_plant2_back)
print("Distance(in x) from plant3(back) for fruit type '1':",xdistance_for_1_from_plant3_back)
print("Distance(in x) from plant3(back) for fruit type '2':",xdistance_for_2_from_plant3_back)

#this is for the distance for the objects in classes '1' and '2' for the plants(front angle)(in y)
for i in range(int(len(idx_for_3_front_sortedInX))):
    y_for_3.append(int(coor_center[idx_for_3_front_sortedInX[i]][1]))
    if(i==0):
        for j in range(len(idx_for_1_inside_plant1_front)):
            y_for_1.append(int(coor_center[idx_for_1_inside_plant1_front[j]][1]))
            ydistance_for_1_from_plant1_front.append(int(math.dist(y_for_3,y_for_1)))
            y_for_1.clear()
        for j in range(len(idx_for_2_inside_plant1_front)):
            y_for_2.append(int(coor_center[idx_for_2_inside_plant1_front[j]][1]))
            ydistance_for_2_from_plant1_front.append(int(math.dist(y_for_3,y_for_2)))
            y_for_2.clear()
        y_for_3.clear()

    if(i==1):
        for j in range(len(idx_for_1_inside_plant2_front)):
            y_for_1.append(int(coor_center[idx_for_1_inside_plant2_front[j]][1]))
            ydistance_for_1_from_plant2_front.append(int(math.dist(y_for_3,y_for_1)))
            y_for_1.clear()
        for j in range(len(idx_for_2_inside_plant2_front)):
            y_for_2.append(int(coor_center[idx_for_2_inside_plant2_front[j]][1]))
            ydistance_for_2_from_plant2_front.append(int(math.dist(y_for_3,y_for_2)))
            y_for_2.clear()
        y_for_3.clear()

    if(i==2):
        for j in range(len(idx_for_1_inside_plant3_front)):
            y_for_1.append(int(coor_center[idx_for_1_inside_plant3_front[j]][1]))
            ydistance_for_1_from_plant3_front.append(int(math.dist(y_for_3,y_for_1)))
            y_for_1.clear()
        for j in range(len(idx_for_2_inside_plant3_front)):
            y_for_2.append(int(coor_center[idx_for_2_inside_plant3_front[j]][1]))
            ydistance_for_2_from_plant3_front.append(int(math.dist(y_for_3,y_for_2)))
            y_for_2.clear()
        y_for_3.clear()


#this is for the distance for the objects in classes '1' and '2' for the plants(back angle)(in y)
for i in range(int(len(idx_for_3_back_sortedInX))):
    y_for_3.append(int(coor_center1[idx_for_3_back_sortedInX[i]][1]))
    if(i==0):
        for j in range(len(idx_for_1_inside_plant1_back)):
            y_for_1.append(int(coor_center1[idx_for_1_inside_plant1_back[j]][1]))
            ydistance_for_1_from_plant1_back.append(int(math.dist(y_for_3,y_for_1)))
            y_for_1.clear()
        for j in range(len(idx_for_2_inside_plant1_back)):
            y_for_2.append(int(coor_center1[idx_for_2_inside_plant1_back[j]][1]))
            ydistance_for_2_from_plant1_back.append(int(math.dist(y_for_3,y_for_2)))
            y_for_2.clear()
        y_for_3.clear()

    if(i==1):
        for j in range(len(idx_for_1_inside_plant2_back)):
            y_for_1.append(int(coor_center1[idx_for_1_inside_plant2_back[j]][1]))
            ydistance_for_1_from_plant2_back.append(int(math.dist(y_for_3,y_for_1)))
            y_for_1.clear()
        for j in range(len(idx_for_2_inside_plant2_back)):
            y_for_2.append(int(coor_center1[idx_for_2_inside_plant2_back[j]][1]))
            ydistance_for_2_from_plant2_back.append(int(math.dist(y_for_3,y_for_2)))
            y_for_2.clear()
        y_for_3.clear()

    if(i==2):
        for j in range(len(idx_for_1_inside_plant3_back)):
            y_for_1.append(int(coor_center1[idx_for_1_inside_plant3_back[j]][1]))
            ydistance_for_1_from_plant3_back.append(int(math.dist(y_for_3,y_for_1)))
            y_for_1.clear()
        for j in range(len(idx_for_2_inside_plant3_back)):
            y_for_2.append(int(coor_center1[idx_for_2_inside_plant3_back[j]][1]))
            ydistance_for_2_from_plant3_back.append(int(math.dist(y_for_3,y_for_2)))
            y_for_2.clear()
        y_for_3.clear()




print("Distance(in y) from plant1(front) for fruit type '1':",ydistance_for_1_from_plant1_front)
print("Distance(in y) from plant1(front) for fruit type '2':",ydistance_for_2_from_plant1_front)
print("Distance(in y) from plant2(front) for fruit type '1':",ydistance_for_1_from_plant2_front)
print("Distance(in y) from plant2(front) for fruit type '2':",ydistance_for_2_from_plant2_front)
print("Distance(in y) from plant3(front) for fruit type '1':",ydistance_for_1_from_plant3_front)
print("Distance(in y) from plant3(front) for fruit type '2':",ydistance_for_2_from_plant3_front)
print("Distance(in y) from plant1(back) for fruit type '1':",ydistance_for_1_from_plant1_back)
print("Distance(in y) from plant1(back) for fruit type '2':",ydistance_for_2_from_plant1_back)
print("Distance(in y) from plant2(back) for fruit type '1':",ydistance_for_1_from_plant2_back)
print("Distance(in y) from plant2(back) for fruit type '2':",ydistance_for_2_from_plant2_back)
print("Distance(in y) from plant3(back) for fruit type '1':",ydistance_for_1_from_plant3_back)
print("Distance(in y) from plant3(back) for fruit type '2':",ydistance_for_2_from_plant3_back)


       
#this is to find the number of elements double counted (with error)
for i in range(len(ydistance_for_1_from_plant1_front)):
    for j in range(len(ydistance_for_1_from_plant1_back)):
        if((abs(ydistance_for_1_from_plant1_front[i]-ydistance_for_1_from_plant1_back[j])<=3) and (abs(xdistance_for_1_from_plant1_front[i]-xdistance_for_1_from_plant1_back[j])<=4)):
            to_substract_1_from_plant1+=1

for i in range(len(ydistance_for_2_from_plant1_front)):
    for j in range(len(ydistance_for_2_from_plant1_back)):
        if(abs(ydistance_for_2_from_plant1_front[i]-ydistance_for_2_from_plant1_back[j]<=3) and (abs(xdistance_for_2_from_plant1_front[i]-xdistance_for_2_from_plant1_back[j])<=4)):
            to_substract_2_from_plant1+=1

for i in range(len(ydistance_for_1_from_plant2_front)):
    for j in range(len(ydistance_for_1_from_plant2_back)):
        if((abs(ydistance_for_1_from_plant2_front[i]-ydistance_for_1_from_plant2_back[j])<=3) and (abs(xdistance_for_1_from_plant2_front[i]-xdistance_for_1_from_plant2_back[j])<=4)):
            to_substract_1_from_plant2+=1

for i in range(len(ydistance_for_2_from_plant2_front)):
    for j in range(len(ydistance_for_2_from_plant2_back)):
        if(abs(ydistance_for_2_from_plant2_front[i]-ydistance_for_2_from_plant2_back[j]<=3) and (abs(xdistance_for_2_from_plant2_front[i]-xdistance_for_2_from_plant2_back[j])<=4)):
            to_substract_2_from_plant2+=1

for i in range(len(ydistance_for_1_from_plant3_front)):
    for j in range(len(ydistance_for_1_from_plant3_back)):
        if((abs(ydistance_for_1_from_plant3_front[i]-ydistance_for_1_from_plant3_back[j])<=3) and (abs(xdistance_for_1_from_plant3_front[i]-xdistance_for_1_from_plant3_back[j])<=4)):
            to_substract_1_from_plant3+=1

for i in range(len(ydistance_for_2_from_plant3_front)):
    for j in range(len(ydistance_for_2_from_plant3_back)):
        if(abs(ydistance_for_2_from_plant3_front[i]-ydistance_for_2_from_plant3_back[j]<=3) and (abs(xdistance_for_2_from_plant3_front[i]-xdistance_for_2_from_plant3_back[j])<=4)):
            to_substract_2_from_plant3+=1


print("Total count of fruit '1' in Plant1:",len(idx_for_1_inside_plant1_front)+len(idx_for_1_inside_plant1_back)-to_substract_1_from_plant1)
print("Total count of fruit '2' in Plant1:",len(idx_for_2_inside_plant1_front)+len(idx_for_2_inside_plant1_back)-to_substract_2_from_plant1)
print("Total count of fruit '1' in Plant2:",len(idx_for_1_inside_plant2_front)+len(idx_for_1_inside_plant2_back)-to_substract_1_from_plant2)
print("Total count of fruit '2' in Plant2:",len(idx_for_2_inside_plant2_front)+len(idx_for_2_inside_plant2_back)-to_substract_2_from_plant2)
print("Total count of fruit '1' in Plant3:",len(idx_for_1_inside_plant3_front)+len(idx_for_1_inside_plant3_back)-to_substract_1_from_plant3)
print("Total count of fruit '2' in Plant3:",len(idx_for_2_inside_plant3_front)+len(idx_for_2_inside_plant3_back)-to_substract_2_from_plant3)
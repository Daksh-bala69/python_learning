import numpy as np
import cv2
import math


from ultralytics import YOLO
model=YOLO("C:\\Users\\BEAST SSJ3\\Downloads\\best.pt")
results=model.predict(r"C:\Users\BEAST SSJ3\Downloads\UAS_DTU_Round_2_Task_data\UAS_DTU_Round_2_Task_data\2\images_close_img_7_4(1).jpg",save=True)

for result in results:
    print(result.boxes.numpy)


#count for all the objects
count_for1=0
count_for2=0
count_for3=0

#list of indexes of occurances of each object in the cls array
idx_for_1=[]
idx_for_2=[]
idx_for_3=[]

#list of indexes of occurances of each object in the cls array but this time image specific
idx_for_1_inside_plant1=[]
idx_for_2_inside_plant1=[]
idx_for_1_inside_plant2=[]
idx_for_2_inside_plant2=[]

#list of temporary x values for each object
x_for_3=[]
x_for_2=[]
x_for_1=[]

#list of temporary y valuas for each object
y_for_3=[]
y_for_2=[]
y_for_1=[]

#list of distance(in x) from the centre of the '3' class object to the centre of the fruits (2,3) in a image specific manner
xdistance_for_1_from_3_angle1=[]
xdistance_for_1_from_3_angle2=[]
xdistance_for_2_from_3_angle1=[]
xdistance_for_2_from_3_angle2=[]

#list of distance(in y) from the centre of the '3' class object to the centre of the fruits (2,3) in a image specific manner
ydistance_for_1_from_3_angle1=[]
ydistance_for_1_from_3_angle2=[]
ydistance_for_2_from_3_angle1=[]
ydistance_for_2_from_3_angle2=[]

#double counted elements which are to be substracted
to_substract_from_1=0
to_substract_from_2=0

#array of the classes of each object detected
arr=result.boxes.cls.cpu().numpy()

#array of the xyxy format coordinates of each object
coor_xy=result.boxes.xyxy.cpu().numpy()

#array of the xywh format coordinates of each object
coor_center=result.boxes.xywh.cpu().numpy()

#loop to find the index and the initial count of the obects according to their classes (including doubly counted elemts)
for i in range(arr.size):
    if(arr[i]==1):
        count_for1+=1
        idx_for_1.append(i)

    if(arr[i]==2):
        count_for2+=1
        idx_for_2.append(i)

    if(arr[i]==3):
        count_for3+=1
        idx_for_3.append(i)

#loop to fint he index of each ojbets but specific to the image/angle by checking which objects lie inside the class '3'objects
for j in range(int(len(idx_for_1))):
    if(coor_xy[0][0]<=coor_xy[idx_for_1[j]][0] and coor_xy[0][1]<=coor_xy[idx_for_1[j]][1] and coor_xy[0][2]>=coor_xy[idx_for_1[j]][2] and coor_xy[0][3]>=coor_xy[idx_for_1[j]][3]):
        idx_for_1_inside_plant1.append(idx_for_1[j])

for j in range(int(len(idx_for_1))):
    if(coor_xy[1][0]<=coor_xy[idx_for_1[j]][0] and coor_xy[1][1]<=coor_xy[idx_for_1[j]][1] and coor_xy[1][2]>=coor_xy[idx_for_1[j]][2] and coor_xy[1][3]>=coor_xy[idx_for_1[j]][3]):
        idx_for_1_inside_plant2.append(idx_for_1[j])

for j in range(int(len(idx_for_2))):
    if(coor_xy[0][0]<=coor_xy[idx_for_2[j]][0] and coor_xy[0][1]<=coor_xy[idx_for_2[j]][1] and coor_xy[0][2]>=coor_xy[idx_for_2[j]][2] and coor_xy[0][3]>=coor_xy[idx_for_2[j]][3]):
        idx_for_2_inside_plant1.append(idx_for_2[j])

for j in range(int(len(idx_for_2))):
    if(coor_xy[1][0]<=coor_xy[idx_for_2[j]][0] and coor_xy[1][1]<=coor_xy[idx_for_2[j]][1] and coor_xy[1][2]>=coor_xy[idx_for_2[j]][2] and coor_xy[1][3]>=coor_xy[idx_for_2[j]][3]):
        idx_for_2_inside_plant2.append(idx_for_2[j])


print("1 inside plant1:",idx_for_1_inside_plant1)
print("1 inside plant2:",idx_for_1_inside_plant2)
print("2 inside plant1:",idx_for_2_inside_plant1)
print("2 inside plant2:",idx_for_2_inside_plant2)


#this is for the distance for the objects in classes '1' and '2' for the first plant(front angle)(in x)
x_for_3.append(int(coor_center[idx_for_3[0]][0]))
for j in range(len(idx_for_1_inside_plant1)):
    x_for_1.append(int(coor_center[idx_for_1_inside_plant1[j]][0]))
    xdistance_for_1_from_3_angle1.append(int(math.dist(x_for_3,x_for_1)))
    x_for_1.clear()
for j in range(len(idx_for_2_inside_plant1)):
    x_for_2.append(int(coor_center[idx_for_2_inside_plant1[j]][0]))
    xdistance_for_2_from_3_angle1.append(int(math.dist(x_for_3,x_for_2)))
    x_for_2.clear()
x_for_3.clear()
print("Distance(in x) from one plant for fruit type '1':",xdistance_for_1_from_3_angle1)
print("Distance(in x) from one plant for fruit type '2':",xdistance_for_2_from_3_angle1)

#this is for the distance for the objects in classes '1' and '2' for the first plant(back angle)(in x)
x_for_3.append(int(coor_center[idx_for_3[1]][0]))
for j in range(len(idx_for_1_inside_plant2)):
    x_for_1.append(int(coor_center[idx_for_1_inside_plant2[j]][0]))
    xdistance_for_1_from_3_angle2.append(int(math.dist(x_for_3,x_for_1)))
    x_for_1.clear()
for j in range(len(idx_for_2_inside_plant2)):
    x_for_2.append(int(coor_center[idx_for_2_inside_plant2[j]][0]))
    xdistance_for_2_from_3_angle2.append(int(math.dist(x_for_3,x_for_2)))
    x_for_2.clear()
x_for_3.clear()
print("Distance(in x) from second plant for fruit type '1':",xdistance_for_1_from_3_angle2)
print("Distance(in x) from second plant for fruit type '2':",xdistance_for_2_from_3_angle2)






#this is for the distance for the objects in classes '1' and '2' for the first plant(front angle)(in y)
y_for_3.append(int(coor_center[idx_for_3[0]][1]))
for j in range(len(idx_for_1_inside_plant1)):
    y_for_1.append(int(coor_center[idx_for_1_inside_plant1[j]][1]))
    ydistance_for_1_from_3_angle1.append(int(math.dist(y_for_3,y_for_1)))
    y_for_1.clear()
for j in range(len(idx_for_2_inside_plant1)):
    y_for_2.append(int(coor_center[idx_for_2_inside_plant1[j]][1]))
    ydistance_for_2_from_3_angle1.append(int(math.dist(y_for_3,y_for_2)))
    y_for_2.clear()
y_for_3.clear()
print("Distance(in y) from one plant for fruit type '1':",ydistance_for_1_from_3_angle1)
print("Distance(in y) from one plant for fruit type '2':",ydistance_for_2_from_3_angle1)

#this is for the distance for the objects in classes '1' and '2' for the first plant(back angle)(in y)
y_for_3.append(int(coor_center[idx_for_3[1]][1]))
for j in range(len(idx_for_1_inside_plant2)):
    y_for_1.append(int(coor_center[idx_for_1_inside_plant2[j]][1]))
    ydistance_for_1_from_3_angle2.append(int(math.dist(y_for_3,y_for_1)))
    y_for_1.clear()
for j in range(len(idx_for_2_inside_plant2)):
    y_for_2.append(int(coor_center[idx_for_2_inside_plant2[j]][1]))
    ydistance_for_2_from_3_angle2.append(int(math.dist(y_for_3,y_for_2)))
    y_for_2.clear()
y_for_3.clear()
print("Distance(in y) from second plant for fruit type '1':",ydistance_for_1_from_3_angle2)
print("Distance(in y) from second plant for fruit type '2':",ydistance_for_2_from_3_angle2)
       
#this is to find the number of elements double counted (with error)
for i in range(len(ydistance_for_1_from_3_angle1)):
    for j in range(len(ydistance_for_1_from_3_angle2)):
        if((abs(ydistance_for_1_from_3_angle1[i]-ydistance_for_1_from_3_angle2[j])<=2) and (abs(xdistance_for_1_from_3_angle1[i]-xdistance_for_1_from_3_angle2[j])<=3)):
            to_substract_from_1+=1

for i in range(len(ydistance_for_2_from_3_angle1)):
    for j in range(len(ydistance_for_2_from_3_angle2)):
        if(abs(ydistance_for_2_from_3_angle1[i]-ydistance_for_2_from_3_angle2[j]<=2) and (abs(xdistance_for_2_from_3_angle1[i]-xdistance_for_2_from_3_angle2[j])<=3)):
            to_substract_from_2+=1



        
print("The count for the yellow fruits:",count_for1-to_substract_from_1)
print("The count for the purple fruits:",count_for2-to_substract_from_2)
print(count_for3)
import numpy as np
import cv2
import math


from ultralytics import YOLO
model=YOLO("C:\\Users\\BEAST SSJ3\\Downloads\\best.pt")
results=model.predict(r"C:\Users\BEAST SSJ3\Downloads\UAS_DTU_Round_2_Task_data\UAS_DTU_Round_2_Task_data\6\images_close_img_21_2.jpg",save=False)

for result in results:
    print(result.boxes.numpy)

count_for1=0
count_for2=0
count_for3=0

idx_for_1=[]
idx_for_2=[]
idx_for_3=[]

idx_for_1_inside_plant1=[]
idx_for_2_inside_plant1=[]
idx_for_1_inside_plant2=[]
idx_for_2_inside_plant2=[]

x_for_3=[]
x_for_2=[]
x_for_1=[]

y_for_3=[]
y_for_2=[]
y_for_1=[]

xdistance_for_1_from_3_angle1=[]
xdistance_for_1_from_3_angle2=[]
xdistance_for_2_from_3_angle1=[]
xdistance_for_2_from_3_angle2=[]

ydistance_for_1_from_3_angle1=[]
ydistance_for_1_from_3_angle2=[]
ydistance_for_2_from_3_angle1=[]
ydistance_for_2_from_3_angle2=[]

to_substract_from_1=0
to_substract_from_2=0

arr=result.boxes.cls.cpu().numpy()
coor_xy=result.boxes.xyxy.cpu().numpy()
coor_center=result.boxes.xywh.cpu().numpy()

print(arr)

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


#this is for the first plant(front angle)
x_for_3.append(int(coor_center[idx_for_3[0]][0]))
for j in range(len(idx_for_1_inside_plant1)):
    x_for_1.append(int(coor_center[idx_for_1_inside_plant1[j]][0]))
    xdistance_for_1_from_3_angle1.append(int(math.dist(x_for_3,x_for_1)))
    x_for_1.clear()
for z in range(len(idx_for_2_inside_plant1)):
    x_for_1.append(int(coor_center[idx_for_2_inside_plant1[j]][0]))
    xdistance_for_2_from_3_angle1.append(int(math.dist(x_for_3,x_for_2)))
    x_for_2.clear()
x_for_3.clear()
print("Distance(in x) from one plant for fruit type '1':",xdistance_for_1_from_3_angle1)
print("Distance(in x) from one plant for fruit type '2':",xdistance_for_2_from_3_angle1)

#this is the for second plant (back angle)
x_for_3.append(int(coor_center[idx_for_3[1]][0]))
for j in range(len(idx_for_1_inside_plant2)):
    x_for_1.append(int(coor_center[idx_for_1_inside_plant2[j]][0]))
    xdistance_for_1_from_3_angle2.append(int(math.dist(x_for_3,x_for_1)))
    x_for_1.clear()
for z in range(len(idx_for_2_inside_plant2)):
    x_for_1.append(int(coor_center[idx_for_2_inside_plant2[j]][0]))
    xdistance_for_2_from_3_angle2.append(int(math.dist(x_for_3,x_for_2)))
    x_for_2.clear()
x_for_3.clear()
print("Distance(in x) from second plant for fruit type '1':",xdistance_for_1_from_3_angle2)
print("Distance(in x) from second plant for fruit type '2':",xdistance_for_2_from_3_angle2)






#this is for plant one(front angle)
y_for_3.append(int(coor_center[idx_for_3[0]][1]))
for j in range(len(idx_for_1_inside_plant1)):
    y_for_1.append(int(coor_center[idx_for_1_inside_plant1[j]][1]))
    ydistance_for_1_from_3_angle1.append(int(math.dist(y_for_3,y_for_1)))
    y_for_1.clear()
for z in range(len(idx_for_2_inside_plant1)):
    y_for_1.append(int(coor_center[idx_for_2_inside_plant1[j]][1]))
    ydistance_for_2_from_3_angle1.append(int(math.dist(y_for_3,y_for_2)))
    y_for_2.clear()
y_for_3.clear()
print("Distance(in y) from one plant for fruit type '1':",ydistance_for_1_from_3_angle1)
print("Distance(in y) from one plant for fruit type '2':",ydistance_for_2_from_3_angle1)

#this is for plant 2 (back angle)
y_for_3.append(int(coor_center[idx_for_3[1]][1]))
for j in range(len(idx_for_1_inside_plant2)):
    y_for_1.append(int(coor_center[idx_for_1_inside_plant2[j]][1]))
    ydistance_for_1_from_3_angle2.append(int(math.dist(y_for_3,y_for_1)))
    y_for_1.clear()
for z in range(len(idx_for_2_inside_plant2)):
    y_for_1.append(int(coor_center[idx_for_2_inside_plant2[j]][1]))
    ydistance_for_2_from_3_angle2.append(int(math.dist(y_for_3,y_for_2)))
    y_for_2.clear()
y_for_3.clear()
print("Distance(in y) from second plant for fruit type '1':",ydistance_for_1_from_3_angle2)
print("Distance(in y) from second plant for fruit type '2':",ydistance_for_2_from_3_angle2)
       
for i in range(len(ydistance_for_1_from_3_angle1)):
    for j in range(len(ydistance_for_1_from_3_angle2)):
        if((abs(ydistance_for_1_from_3_angle1[i]-ydistance_for_1_from_3_angle2[j])<=2) and (abs(xdistance_for_1_from_3_angle1[i]-xdistance_for_1_from_3_angle2[j])<=3)):
            to_substract_from_1+=1

for i in range(len(ydistance_for_2_from_3_angle1)):
    for j in range(len(ydistance_for_2_from_3_angle2)):
        if(abs(ydistance_for_2_from_3_angle1[i]-ydistance_for_2_from_3_angle2[j]<=2) and abs(xdistance_for_2_from_3_angle1[i]-xdistance_for_2_from_3_angle2[j])):
            to_substract_from_2+=1



        


print(idx_for_1)
print(idx_for_2)
print(idx_for_3)


print("The count for the yellow fruits:",count_for1-to_substract_from_1)
print("The count for the purple fruits:",count_for2-to_substract_from_2)
print(count_for3)
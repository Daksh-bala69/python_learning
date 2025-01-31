import numpy as np
import cv2


from ultralytics import YOLO
model=YOLO("C:\\Users\\BEAST SSJ3\\Downloads\\best.pt")
results=model.predict(r"C:\Users\BEAST SSJ3\Downloads\UAS_DTU_Round_2_Task_data\UAS_DTU_Round_2_Task_data\8\imageuptodown_img_7_4.jpg",save=False)

for result in results:
    print(result.boxes.numpy)

count_for0=0
count_for1=0
count_for2=0
count_for3=0
count_for4=0
count_for5=0

for i in range(3):
    if(result.boxes.cls[int(i)]==0):
        count_for0+=1
    if(result.boxes.cls[int(i)]==1):
        count_for1+=1
    if(result.boxes.cls[int(i)]==2):
        count_for2+=1
    if(result.boxes.cls[int(i)]==3):
        count_for3+=1
    if(result.boxes.cls[int(i)]==4):
        count_for4+=1
    if(result.boxes.cls[int(i)]==5):
        count_for5+=1

print(count_for0)
print(count_for1)
print(count_for2)
print(count_for3)
print(count_for4)
print(count_for5)
import numpy as np
import cv2


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

arr=result.boxes.cls.cpu().numpy()

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

print(idx_for_1)
print(idx_for_2)
print(idx_for_3)


print(count_for1)
print(count_for2)
print(count_for3)

import os
import cv2
path= '/Users/user/Desktop/python_projects/computer_vision/sample-images/'

for i in os.listdir(path):

    img=cv2.imread(path+i,0)
    resized_img = cv2.resize(img,(100,100))
    cv2.imwrite("resized"+i,resized_img)

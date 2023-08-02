from ultralytics import YOLO
import cv2
import numpy as np

capture = cv2.VideoCapture(0)
capture.set(3,720)
capture.set(4,360)

model = YOLO('yolov8n.pt')


success, img =capture.read()
results = model(img, show=True)

# for i in results:
#     x,y,w,h =i.xyxy
#     print(x,y,w,h)

# while True:
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# model = YOLO('yolov8n.pt')
# results = model('1.jpg',show=True)

# cv2.imshow("wewe",results)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# yawaa


from ultralytics import YOLO
import cv2
import numpy as np


model = YOLO('yolov8l.pt')
# results = model('1.jpg',show=True)\

classes = model.model.names
if 'phone' in classes:
    print(classes)

# cv2.imshow("wewe",results)
cv2.waitKey(10)
cv2.destroyAllWindows()



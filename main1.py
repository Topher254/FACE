from ultralytics import YOLO
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 720 ) #set width
cap.set(4, 360) #height

# create model
model = YOLO('yolov8n.pt')

while True:
    success, img = cap.read()
    results= model(img, stream=True)
    # stream uses generators
    # check for individual boxes
    for r in results:
        boxes = r.boxes
        # loop through
        for box in boxes:
            # find x and y coordinates
            x1,y1,x2,y2 = box.xyxy[0]
            a = int(x1) 
            b = int(y1)
            c = int(x2)
            d = int(y2)

            print("cordinates are",int(x1),int(y1),int(x2),int(y2))
            # lets create a rectangle bounded by this cordinates
            # cv2.rectangle(img,((x1,y1)),(0,255,0),3)
            cv2.rectangle(img,(a,b),(c,d),(0,255,0),3)
    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
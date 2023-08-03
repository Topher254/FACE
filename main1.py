from ultralytics import YOLO
import cv2
import pyttsx3
import cvzone

engine = pyttsx3.init()


cap = cv2.VideoCapture(0)
cap.set(3, 720 ) #set width
cap.set(4, 360) #height

classNames = [
    "Person", "chair", "staircase", "water", "pit"
]

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
            

            # percentage confidence values
            confidence = round(box.conf[0].item(),2)
            confidence_display = str(confidence)
            font = cv2.FONT_HERSHEY_PLAIN
            # cv2.putText(img,confidence_display,(a,b),font,2,(255,0,0),3)
            # cvzone.putTextRect(img,confidence_display,(a,b))
            

            # classes
            class_id = box.cls[0].item()
            class_0 = 'Person'
            class_1 = 'Bicyle'
            class_2 = 'Car'
            class_56 = 'Chair'

            print("Class",class_id)
            print("confidence",confidence)
            print("-----")

            if class_id == 0:
                cv2.putText(img,f"{class_0}..{confidence_display}",(a,b),font,2,(0,255,0),3)
                engine.say("Person detected")
                engine.runAndWait()
            if class_id == 1:
                engine.say("Bicycle detected")
                engine.runAndWait()

            if class_id == 3:
                engine.say("Vehicle detected")
                engine.runAndWait()
            if class_id == 56:
                engine.say("Chair detected")
                engine.runAndWait()



    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

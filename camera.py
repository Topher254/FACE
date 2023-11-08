from ultralytics import YOLO
import cv2
import pyttsx3
import cvzone

engine = pyttsx3.init()


cap = cv2.VideoCapture(0)
cap.set(3, 720 ) #set width
cap.set(4, 360) #height

classNames = [
    "Person", "chair", "staircase", "water", "pit","cell_phone", 'TV'
'Laptop','Cow','dog', 'cat'
]

# create model
model = YOLO('yolov8l.pt')


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
            class_67 = 'cell_phone'
            class_62 = 'TV'
            class_63 = 'Laptop'
            class_19 = 'Cow'
            class_16 = 'dog'
            class_15 = 'cat'

            # BACKGROUND OF TEXT
            # not working
            rect_bgr = (77,26,120)
            # cv2.rectangle(img,(a,a+20),(b,b+20),(255,0,0),3)

            print("Class",class_id)
            print("confidence",confidence)
            print("-----")
             
            text_color = (255,0,255)
            if class_id == 0:
                texta = f"{class_0}_{confidence_display}"
                cv2.putText(img,texta,(a,b),font,2,text_color,3)
                engine.say("Person detected")
                cv2.putText(img,texta,(a,b),font,2,text_color,3)fhh
                engine.runAndWait()
            if class_id == 1:
                texta = f"{class_1}_{confidence_display}"
                engine.say("Bicycle detected")
                cv2.putText(img,texta,(a,b),font,2,text_color,3)
                engine.runAndWait()

            if class_id == 3:
                texta = f"{class_2}_{confidence_display}"
                engine.say("Vehicle detected")
                cv2.putText(img,texta,(a,b),font,2,text_color,3)
                engine.runAndWait()
            if class_id == 56:
                texta = f"{class_56}_{confidence_display}"
                engine.say("Chair detected")
                cv2.putText(img,texta,(a,b),font,2,text_color,3)
                engine.runAndWait()

            if class_id == 67:
                texta = f"{class_0}_{confidence_display}"
                cv2.putText(img,texta,(a,b),font,2,text_color,3)
                engine.say("Cell phone detected")
                cv2.putText(img,texta,(a,b),font,2,text_color,3)
                engine.runAndWait()
            if class_id == 62:
                texta = f"{class_1}_{confidence_display}"
                engine.say("Television detected")
                cv2.putText(img,texta,(a,b),font,2,text_color,3)
                engine.runAndWait()

            if class_id == 63:
                texta = f"{class_2}_{confidence_display}"
                engine.say("Laptop detected")
                cv2.putText(img,texta,(a,b),font,2,text_color,3)
                engine.runAndWait()
            if class_id == 19:
                texta = f"{class_56}_{confidence_display}"
                engine.say("Cow detected")
                cv2.putText(img,texta,(a,b),font,2,text_color,3)
                engine.runAndWait()
            if class_id == 16:
                texta = f"{class_0}_{confidence_display}"
                engine.say("Dog detected")
                cv2.putText(img,texta,(a,b),font,2,text_color,3)
                engine.runAndWait()
            if class_id == 15:
                texta = f"{class_1}_{confidence_display}"
                engine.say("CAT detected")
                cv2.putText(img,texta,(a,b),font,2,text_color,3)
                engine.runAndWait()
        

    print("Class",class_id)
    print("confidence",confidence)
    print("-----")

    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

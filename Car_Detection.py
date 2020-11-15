#!/usr/bin/env python
# coding: utf-8

# In[1]:
class cd:
    def car_live_de(self):
        try :
            import cv2
            from time import sleep
            cam = cv2.VideoCapture(0)
            classifier = cv2.CascadeClassifier("cars.xml")
            def working(img):
                sleep(.06)
                img = cv2.resize(img,(600,600))
                cars = classifier.detectMultiScale(img,1.1,2)
                for (x,y,w,h) in cars:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.putText(img,"Car",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,.7,(0,0,255),1)
                return img
            while True:
                temp,img = cam.read()
                if temp:
                    img = working(img)
                    cv2.imshow("Live Car Detection",img)
                    if cv2.waitKey(1)==13:
                        break
                else:
                    return False
            cv2.destroyAllWindows()
            return True
        except:
            return False

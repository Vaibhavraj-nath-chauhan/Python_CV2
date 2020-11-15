#!/usr/bin/env python
# coding: utf-8

# In[3]:


class fd: 
    def face(self):
        try:
            import cv2
            classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            cam  = cv2.VideoCapture(0)
            while True:
                temp , img = cam.read()
                if temp:
                    faces = classifier.detectMultiScale(img,1.3,5)
                    for x,y,w,h in faces:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                        cv2.putText(img,"Detected",(x,y-20),cv2.FONT_HERSHEY_COMPLEX,.6,(0,255,0),1)
                    cv2.imshow("img",img)
                    if cv2.waitKey(1) == 13:
                        break
            cam.release()
            cv2.destroyAllWindows()
            return True
        except:
            return False

        
        


import cv2
import os
import pickle
import face_recognition
import numpy as np
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import numpy as np
from datetime import datetime
import time
from time import sleep
import streamlit as st

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://teha-27d7f-default-rtdb.asia-southeast1.firebasedatabase.app/",
    'storageBucket': "teha-27d7f.appspot.com"
})

bucket = storage.bucket()

cap = cv2.VideoCapture(0)
#grafik size
cap.set(3, 640) 
cap.set(4, 480) 

imgBackground = cv2.imread('Resources/background.png')

folderModePath = 'Resources/Modes'
modePathList = os.listdir (folderModePath)
imgModeList = []
#for path modes
#print(modePathList)
for path in modePathList:
        imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))
#print(len(imgModeList))

#load encoding file
print("Loading Encode file..")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
#print(studentIds)
print("Encode file loaded..")

modeType=-1
counter = 0
id=-1
imgStudent = []

while True:
    success, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    #pasin webcam ama grafik
    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    if faceCurFrame:
        for encodeFace, faceLoc in zip (encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            #print ("matches", matches)
            #print ("faceDis", faceDis)

            matchesIndex = np.argmin(faceDis)
            #print ("Match Index", matchesIndex)

            if matches[matchesIndex]:
                #print("knows face detected")
                #print(studentIds[matchIndex])
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                id = studentIds[matchesIndex]
                if counter == 0:
                    cvzone.putTextRect(imgBackground, "MEMBER DETECTED!", (220, 400),
                    cv2.FONT_HERSHEY_DUPLEX,0,8,(255,255,255),1,5)   
                    #warna         
                    cv2.imshow("Face Attendance", imgBackground)
                    cv2.waitKey (1)
                    counter = 1
                    modeType = 0

        if counter!=0:
            
            if counter ==1:
                #get data
                memberInfo = db.reference(f'Member/{id}').get()
                print(memberInfo)
                #get image from stream
                blob = bucket.get_blob(f'Images/{id}.png')
                array = np.frombuffer(blob.download_as_string(), np.uint8)
                imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)
                #update data yang hadir

                datetimeObject = datetime.strptime(memberInfo['last_attendance_time'],
                                                        "%Y-%m-%d %H:%M:%S")
                secondsElapsed = (datetime.now() - datetimeObject).total_seconds()
                print(secondsElapsed)
                
                if secondsElapsed > 30:
                    ref = db.reference(f'Member/{id}')
                    memberInfo['total_attendance'] +=1
                    ref.child('total_attendance').set(memberInfo['total_attendance'])
                    ref.child('last_attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                else :
                    modeType =2 
                    counter = 0
                    imgBackground[44:44 + 633, 808:808 +414] = imgModeList[modeType]
            
            if modeType != 2:

                if 10<counter<20:
                    modeType =1

                imgBackground[44:44 + 633, 808:808 +414] = imgModeList[modeType]

                if counter<=10:   

                    cv2.putText(imgBackground,str(memberInfo['total_attendance']),(861,125),
                                cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255),1)
                    cv2.putText(imgBackground,str(memberInfo['stages']),(1006,550),
                                cv2.FONT_HERSHEY_DUPLEX,0.5,(255,255,255),1)
                    cv2.putText(imgBackground,str(id),(1006,493),
                                cv2.FONT_HERSHEY_DUPLEX,0.5,(255,255,255),1)
                    cv2.putText(imgBackground,str(memberInfo['starting_year']),(1125,625),
                                cv2.FONT_HERSHEY_DUPLEX,0.6,(100,100,100),1)
                    cv2.putText(imgBackground,str(memberInfo['level']),(910,625),
                                cv2.FONT_HERSHEY_DUPLEX,0.6,(100,100,100),1)
                    cv2.putText(imgBackground,str(memberInfo['ig']),(1025,625),
                                cv2.FONT_HERSHEY_DUPLEX,0.6,(100,100,100),1)
                    
                    (w, h), _ = cv2.getTextSize(memberInfo['name'],
                        cv2.FONT_HERSHEY_DUPLEX, 1, 1)
                    offset = (414 - w) // 2
                    cv2.putText(imgBackground, str(memberInfo['name']), (808 + offset, 445),
                        cv2.FONT_HERSHEY_DUPLEX, 1, (50, 50, 50), 1)

                    imgBackground [175:175+216, 909:909+216] = imgStudent
                    cv2.waitKey(200)
                    
                counter+= 1

                if counter>=20:
                        counter = 0
                        modeType = -1
                        memberInfo = []
                        imgStudent = []
                        imgBackground[44:44 + 633, 808:808 +414] = imgModeList[modeType]
    else:
        modeType = -1
        counter = 0 

    #cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)

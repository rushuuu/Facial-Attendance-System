import numpy as np
import face_recognition
import cv2 as cv
import csv
import os
from datetime import datetime
 
video_capture = cv.VideoCapture(0)
 
Rushil = face_recognition.load_image_file("location_of_file.jpeg")
rushil_en = face_recognition.face_encodings(Rushil)[0]
 
known_face_encoding = [
rushil_en
]
 
known_faces_names = [
"Rushil"
]

roll = {"Rushil" : "roll_no"}
 
students = known_faces_names.copy()
 
face_locations = []
face_encodings = []
face_names = []
s=True
 
now = datetime.now()
current_date = now.strftime("%d-%m-%Y")
 
f = open(current_date+'.csv','a',newline = '')
lnwriter = csv.writer(f)
 
while True:
    _,frame = video_capture.read()
    small_frame = cv.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = small_frame[:,:,::-1]
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
            name=""
            face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]
 
            face_names.append(name)
            if name in known_faces_names:
                font = cv.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,100)
                fontScale              = 1.5
                fontColor              = (0,0,0)
                thickness              = 3
                lineType               = 2
 
                cv.putText(frame,name+' is Present' , 
                    bottomLeftCornerOfText, 
                    font, 
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)
 
                if name in students:
                    students.remove(name)
                    print("Absentees : ",students)
                    current_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                    lnwriter.writerow([name,current_time,roll[name]])
    cv.imshow("Attendence System",frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
 
video_capture.release()
cv.destroyAllWindows()
f.close()

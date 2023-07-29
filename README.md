# Facial Recognition Attendance System

The Face Recognition Attendance System is a Python program that uses the face_recognition library and OpenCV to perform real-time face recognition and mark attendance for recognized students. The system captures video frames from the webcam, detects faces, and matches them with known student faces to mark their presence.

Features:
Real-time face recognition: The program uses the face_recognition library to detect and recognize faces in real-time from the webcam.
Attendance marking: When a recognized student is detected, the program marks their attendance in a CSV file along with the current date and time.

The following Python libraries are required to run the program:
numpy: For numerical operations.
face_recognition: For face detection and recognition.
cv2 (OpenCV): For capturing video frames and image processing.
csv: For reading and writing attendance data to a CSV file.
os: For file and directory operations.
datetime: For getting the current date and time.

How to Use:
Add Known Students: Before running the program, add the image file containing the face of each known student to the program's directory. Ensure that the image file name corresponds to the name of the student.
Encoding Known Faces: When the program starts, it loads the image files of known students and computes their face encodings. These face encodings are used for face recognition.
Run the Program: Execute the Python script, and the webcam will open, capturing video frames for face recognition.
Face Recognition and Attendance: As students' faces are detected, the program compares them with known faces. If a match is found, the student's name is displayed on the video frame, indicating their presence. Their attendance is then marked in a CSV file with the current date and time.
Exit: To stop the program, press the 'q' key in the webcam window.
CSV File Format:
The attendance data is stored in a CSV file with the name format: DD-MM-YYYY.csv, where DD, MM, and YYYY represent the day, month, and year, respectively. The CSV file contains the following columns:
Student Name: The name of the recognized student.
Date and Time: The date and time when the student was recognized.
Roll Number: The roll number associated with the recognized student.

Note:
The current implementation assumes that there is only one known student in the system. If you want to add multiple students, you would need to update the known_face_encoding, known_faces_names, and roll dictionaries accordingly.The program uses case-insensitive face recognition, meaning it will match names regardless of case (e.g., "Rushil" and "rushil" will be considered the same).This is a basic implementation and may require further optimization and improvements for larger-scale deployment or real-world scenarios.

Author:
The Face Recognition Attendance System is developed by Rushil Prajapati.

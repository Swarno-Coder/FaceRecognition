import cv2
import numpy as np
import face_recognition
import os



imgElon = face_recognition.load_image_file("img/Elon1.jpg")
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file("img/Billgate1.jpg")
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
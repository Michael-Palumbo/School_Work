import face_recognition
import cv2
import os

cam = cv2.VideoCapture(0)

cv2.namedWindow("Photo Capture")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing the program...")
        break
    elif k % 256 == 32:
        # SPACE pressed
        face_encoding = face_recognition.face_encodings(frame)
        if len(face_encoding) > 0:
            student_input = input("Please enter student name:\n")
            student_name = student_input.lower()
            img_name = "{}.jpg".format(student_name)
            #img_name = "Test {}.jpg".format(img_counter)
            cv2.imwrite(os.path.join('Known Photo', img_name), frame)
            img_counter += 1
        else:
            print("No faces found in the image!")

cam.release()
cv2.destroyAllWindows()
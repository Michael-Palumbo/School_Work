import face_recognition
import cv2

new_photo = cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    key = cv2.waitKey(1)
    ret, frame = new_photo.read()
    if key % 256 == 32: # SPACE pressed
        new_face_encoding = face_recognition.face_encodings(frame)
        if len(new_face_encoding) > 0:
            new_face_encoding = new_face_encoding[0] #and then save to file
            cv2.imshow("Student Photo", frame)
            cv2.imwrite('Known Photo/new_image.png', frame)
        else:
            cv2.putText(frame, "No Face Detected", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255))
    elif key % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

new_photo.release()
cv2.destroyAllWindows()

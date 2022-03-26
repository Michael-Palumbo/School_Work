import face_recognition
import cv2

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file("Known Photo/obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
biden_image = face_recognition.load_image_file("Known Photo/biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

me_image = face_recognition.load_image_file("Known Photo/me.jpg")
me_face_encoding = face_recognition.face_encodings(me_image)[0]

michael_image = face_recognition.load_image_file("Known Photo/michael.jpg")
michael_face_encoding = face_recognition.face_encodings(michael_image)[0]

tammy_image = face_recognition.load_image_file("Known Photo/parker.jpg")
tammy_face_encoding = face_recognition.face_encodings(tammy_image)[0]

chance_image = face_recognition.load_image_file("Known Photo/chance.jpg")
chance_face_encoding = face_recognition.face_encodings(chance_image)[0]

nathan_image = face_recognition.load_image_file("Known Photo/nathan beebe.jpg")
nathan_face_encoding = face_recognition.face_encodings(nathan_image)[0]

new1_image = face_recognition.load_image_file("Known Photo/joey arnold.jpg")
new1_face_encoding = face_recognition.face_encodings(new1_image)[0]

new2_image = face_recognition.load_image_file("Known Photo/yangmeng shi.jpg")
new2_face_encoding = face_recognition.face_encodings(new2_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding,
    me_face_encoding,
    michael_face_encoding,
    tammy_face_encoding,
    chance_face_encoding,
    nathan_face_encoding,
    new1_face_encoding,
    new2_face_encoding
]
known_face_names = [
    "Barack Obama",
    "Joe Biden",
    "Steven Nie",
    "Michael",
    "Parker",
    "Chance",
    "Nathan Beebe",
    "Joey Arnold",
    "Shi Yangmeng"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 100, 100), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 100, 100), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) % 256 == 27:
        print("You hit Esc, will exit now...")
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
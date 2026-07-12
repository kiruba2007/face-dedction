import cv2

alg = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)

cam = cv2.VideoCapture(0)  # Changed 1 → 0

if not cam.isOpened():
    print("Error: Camera not found!")
    exit()

while True:
    success, img = cam.read()

    if not success:  # Add this check
        print("Failed to read frame from camera")
        break

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face = haar_cascade.detectMultiScale(grayImg, 1.3, 4)

    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.imshow("FaceDetection", img)

    key = cv2.waitKey(10)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()

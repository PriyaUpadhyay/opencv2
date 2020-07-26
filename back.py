import cv2
# THIS IS MY WEBCAM
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read()
    # BACK IS WHAT CAMERA IS READING
    if ret:
        cv2.imshow("image",back)
        if cv2.waitKey(5)== ord('q'):
            # SAVE THE IMAGE
            cv2.imwrite('image.jpg',back)
            break

cap.release()
cv2.destryAllWindows()
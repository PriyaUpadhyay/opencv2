import cv2
import numpy as np
cap = cv2.VideoCapture(0)
back = cv2.imread('./image.jpg')

while cap.isOpened():
    # take each frame
    ret, frame = cap.read()

    if ret:
        # how to convert rgb to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv", hsv)

        # how to get hsv value?
        # lower: hue-10,100,100 higher: h+10, 255,255
        red = np.uint8([[[0,0,255]]])
        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)

        # print(hsv_red)
        # threshold the hsv value to get only red color
        l_red = np.array([0,100,100])
        u_red = np.array([10,255,255])

        mask = cv2.inRange(hsv, l_red, u_red)
        #cv2.imshow("mask",mask)

        # part1 is all things red
        part1 = cv2.bitwise_and(back, back, mask=mask)
        kernel = np.ones((5,5), np.uint8)
        clos = cv2.morphologyEx(part1, cv2.MORPH_CLOSE, kernel)
        closing = cv2.morphologyEx(clos,cv2.MORPH_CLOSE,kernel)
        #cv2.imshow("part1", part1)

        mask =cv2.bitwise_not(mask)

        # part2 is all things not red
        part2 = cv2.bitwise_and(frame, frame , mask=mask)
        #cv2.imshow("mask", part2)
        cloak = closing+part2


        cv2.imshow("cloak", cloak)

        if cv2.waitKey(5) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()


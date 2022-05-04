import cv2

cap = cv2.VideoCapture("./ae.mp4")
c = 1

FPS = cap.get(5)
print(FPS)
frameRate = 1

while(True):
    ret, frame = cap.read()
    if ret:
        if(c % frameRate == 0):
            print(str(c) + " 帧")
            cv2.imwrite("./pic/" + str(c) + '.jpg', frame)
        c += 1
        cv2.waitKey(0)
    else:
        break
cap.release()

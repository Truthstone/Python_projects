import cv2

vc = cv2.VideoCapture(0)
vc.set(3, 1280)
vc.set(4, 720)
while True:
    _, frame = vc.read()
    sx = cv2.Canny(frame, 100, 200)
    cv2.imshow("Res", sx)
    if cv2.waitKey(30) & 0xff == 27:
        break
vc.release()
cv2.destroyAllWindows()

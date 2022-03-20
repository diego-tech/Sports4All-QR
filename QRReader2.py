from time import sleep
import cv2

cap = cv2.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

while True:
    _, img = cap.read()

    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)
    # check if there is a QRCode in the image
    if data:
        a = data
        print("Data: ", a)
        sleep(3)

    # cv2.imshow("QRCODEscanner", img)
    if cv2.waitKey(1) == ord("q"):
        break

    if a == 3522:
        print("Correcto")
    else:
        print("No")

cap.release()
cv2.destroyAllWindows()

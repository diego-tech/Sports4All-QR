from QrSystem import networkmanager, sensors
import cv2
import time


def readQr():
    cap = cv2.VideoCapture(0)

    # Initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()

    # Initialize Qr Code Variable
    codeReader = ""
    while True:
        _, img = cap.read()

        # detect and decode
        data, bbox, _ = detector.detectAndDecode(img)
        # check if there is a QRCode in the image
        if data:
            codeReader = data
            print("Qr Code Value: ", codeReader)
            checkStatus()
            time.sleep(3)

        # cv2.imshow("QRCODEscanner", img)
        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

def checkStatus():
    status = networkmanager.qrValidation()

    if status == 1:
        print("Código Válido")
        sensors.buzzerOn()
        sensors.sensorOn()
        sensors.sensorOff()
    elif status == 0:
        print("Código No Válido")
        sensors.buzzerOn()
        sensors.sensorOff()

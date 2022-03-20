from QrSystem import networkmanager
import cv2


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
            checkStatus()
            print("Qr Code Value: ", codeReader)

        # cv2.imshow("QRCODEscanner", img)
        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

def checkStatus():
    status = networkmanager.qrValidation()

    if status == 1:
        print("Adelante")
    elif status == 0:
        print("No Puede")

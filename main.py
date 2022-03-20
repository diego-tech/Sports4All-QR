from QrSystem import qr_reader, sensors

# Functions
def readQr():
    sensors.setPines()
    qr_reader.readQr()
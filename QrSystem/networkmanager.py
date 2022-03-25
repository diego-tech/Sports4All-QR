import requests
import json

url = "http://ec2-3-8-102-5.eu-west-2.compute.amazonaws.com/api/qrvalidation"

def qrValidation(qrCode):
    params = {'qr': qrCode}
    request = requests.post(url, data = params)
    print(request)

    # Test With Mock Dictionary
    # mockDictionary = {
    #     "status": 1,
    #     "msg": "Puerta abierta"
    # }

    status = request['status']
    print("Status :", status)

    return status
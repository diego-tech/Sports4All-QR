import requests
import json

url = "http://ec2-3-8-102-5.eu-west-2.compute.amazonaws.com/api/qrvalidation"

def qrValidation(qrCode):
    params = {'qr': qrCode}
    request = requests.post(url, data = params)
    jsonLoad = request.json()
    
    status = jsonLoad['status']
    print("Status :", status)

    return status
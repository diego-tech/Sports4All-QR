import requests
import json

url = 'https://www.w3schools.com/python/demopage.php'

def qrValidation():
    # params = {'qr': qrCode}
    # request = requests.post(url, data = params)

    # Test With Mock Json
    mockFile = "../mockresponse.json"

    with open(mockFile) as mf:
        data = json.load(mf)
        status = data['status']
        print("Status :", status)
        return status
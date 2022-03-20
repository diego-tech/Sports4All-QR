import requests
import json

url = 'https://www.w3schools.com/python/demopage.php'


def qrValidation():
    # params = {'qr': qrCode}
    # request = requests.post(url, data = params)

    # Test With Mock Dictionary
    mockDictionary = {
        "status": 1,
        "msg": "Puerta abierta"
    }

    status = mockDictionary['status']
    print("Status :", status)

    return status

import requests
import json

# url = 'https://www.w3schools.com/python/demopage.php'

# def qrValidation(qrCode):
#     params = {'qr': qrCode}

#     request = requests.post(url, data = params)

#     print(request)

# qrValidation('12')

mockFile = "../mockresponse.json"

with open(mockFile) as f:
    data = json.load(f)

    print(data['status'])
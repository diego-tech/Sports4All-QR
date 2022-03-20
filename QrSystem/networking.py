import requests
import json

# url = 'https://www.w3schools.com/python/demopage.php'

# def qrValidation(qrCode):
#     params = {'qr': qrCode}

#     request = requests.post(url, data = params)

#     print(request)

# qrValidation('12')

with open('mockresponse.json') as mr:
    data = json.loads(mr)
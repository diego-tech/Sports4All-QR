import requests

url = 'https://www.w3schools.com/python/demopage.php'

def qrValidation(qrCode):
    myobj = {'qr': qrCode}

    x = requests.post(url, data = myobj)

    print(x.text)

qrValidation('12')
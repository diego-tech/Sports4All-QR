from distutils.log import debug
import main
from flask import Flask

app = Flask(__name__)

@app.route("/")
def readQr():
    main.readQr()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)


from distutils.log import debug
import main
from flask import Flask

app = Flask(__name__)

@app.route("/")
def readQr():
    main.readQr()

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from random import randint
app = Flask(__name__)

@app.route('/home') #location for web (endpoint)
def hello_internet():
    return str(randint(0,100))

@app.route('/create/<name>',methods=["GET"])
def hello_i(name):
    name = name.upper()
    return name
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
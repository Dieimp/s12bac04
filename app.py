import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def fibonnaci():
    n = 50
    a = 1
    b = 1
    #chega ao numero de termos que � a
    if n > 1:
        print(a)
        for i in range (2, n +1):
            b = b + a
            a = b - a
            print(a)
    else:
        print(a)
    return 

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    

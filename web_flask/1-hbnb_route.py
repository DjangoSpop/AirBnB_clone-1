#!/usr/bin/python3
from flask import Flask
"""
here we gone route the url to navigate to /hbnb explaining how routing in web sites into many files 

"""

app = Flask(__name__)

@app.route('/',strict_slashes = False)

def hello_hbnb():
    return "Hello HBND!"

@app.route ('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

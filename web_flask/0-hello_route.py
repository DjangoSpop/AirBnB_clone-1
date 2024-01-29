#!/usr/bin/python3
from flask import Flask
"""
we here gone set up routing of urls to make the url more easier to understand and ptofessopnal


"""
app = Flask(__name__)


@app.route('/', strict_slashes= False)

def hello_hbnd():
    return "Hello HBND!"

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5000)

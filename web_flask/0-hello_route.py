#!/usr/bin/python3
from flask import Flask

"""
We here gone set up routing of urls to make the url more easier to understand and ptofessopnal


"""
app = Flask(__name__)


@app.route('/', strict_slashes= False)
"""
The function prints the hello hbnd with flask web framework
"""
def hello_hbnd():
    return "Hello HBND!"
"""
Here we can test condition if the calling of the module is for it abd in main only
"""
if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5000)

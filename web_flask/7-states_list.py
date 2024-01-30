#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""
from flask import Flask, render_template 
from models import DBStorage
from models.state import State

app = Flask(__name__)
appurl_map.strict_slashes = False
app.config['JSON_SORT_KEYS'] = False
storage = DBStorage()
storage.reload()

@app.route('/states_list')
def states_list():
    states = storage.all(State)
    return render_template('states_list.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
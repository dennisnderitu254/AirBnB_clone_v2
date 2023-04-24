#!/usr/bin/python3
"""Starts a flask app
    listens to 0.0.0.0:5000

"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ teardown db"""
    if storage is not None:
        storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ list of state ids"""
    data = storage.all(State)
    return render_template('7-states_list.html', total=data.values())


if __name__ == "__main__":
    app.run(host="0.0.0.0")

#!/usr/bin/python3
"""
Python script that starts a web application
"""


from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_session(exception):
    """function to close the session"""
    storage.close()


@app.route('/cities_by_states')
def call_states():
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

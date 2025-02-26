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


@app.route('/states')
def call_states():
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def call_states_by_id(id=None):
    states = storage.all(State).values()
    newState = None
    for state in states:
        if state.id == id:
            newState = state
    return render_template('9-states.html', newState=newState)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

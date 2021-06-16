import RedfordCommands as redford
import subprocess
import os
import json
import time
import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Redford-Speech</h1><p>This site is a prototype API for Redford.</p>"

# A route to approach Redford from the Matrix local speech client
@app.route('/api/v1/speech', methods=['GET'])
def api_all():
    # here we want to get the value of the recognized command (i.e. ?command=some-value)
    command = request.args.get('command')
    response = subprocess.check_output(f"python3 '/home/surowa/redford-ansible/ai_src/Redford.py' {command} speech", shell=True)
    return f"Command {command} given to Redford: {response}"

app.run(host = '0.0.0.0',port=5000)
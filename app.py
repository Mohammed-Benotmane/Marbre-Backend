import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
import sys
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#db_drop_and_create_all()

## ROUTES
@app.route('/')
def get_marbre():
    return jsonify({
        'success':True,
        'marbre': 'welcome'
    })

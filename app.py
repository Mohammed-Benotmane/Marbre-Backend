import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
import sys
from flask_cors import CORS
from models import db_drop_and_create_all, setup_db, Marbre,db

app = Flask(__name__)
setup_db(app)
CORS(app)

#db_drop_and_create_all()

## ROUTES
@app.route('/')
def get_test():
    return jsonify({
        'success':True,
        'marbre': 'welcome'
    })

@app.route('/marbres',methods=['POST'])
def post_marbre():
    body = request.get_json()
    new_title = body.get("title",None)
    new_image = body.get("image",None)
    new_price = body.get("price",None)
    new_origin = body.get("origin",None)

    try:
        marbre = Marbre(title = new_title,image= new_image, price=new_price, origin=new_origin)
        marbre.insert()
    except:
        print(sys.exc_info())
    return jsonify({
        'Success':True,
        'Marbre': marbre.format()
    })

@app.route('/marbres',methods=['GET'])
def get_marbre():
    marbres = Marbre.query.all()
    formatted_marbres = [marbre.format() for marbre in marbres] 
    return jsonify({
        'Success':True,
        'marbres': formatted_marbres
    })
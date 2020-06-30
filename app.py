import os
from flask import Flask,jsonify,request,abort
from models import setup_db,Marbre
from flask_cors import CORS

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

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
        new_description = body.get("description",None)

        try:
            marbre = Marbre(title = new_title, image= new_image, price=new_price, origin=new_origin, description=new_description)
            marbre.insert()
        except:
            print(" ")
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

    @app.route('/marbres/<marbre_id>',methods=['PATCH'])
    def patch_marbre(marbre_id):
        body = request.get_json()
        marbre = Marbre.query.get(marbre_id)
        if(body.get("title")):
            marbre.title = body.get("title")
        if(body.get("image")):
            marbre.image = body.get("image")
        if(body.get("price")):
            marbre.price = body.get("price")
        if(body.get("origin")):
            marbre.origin = body.get("origin")
        if(body.get("description")):
            marbre.description = body.get("description")
        try:
            marbre.insert()
        except:
            print(" ")
        return jsonify({
            'Success':True,
            'Marbre': marbre.format()
        })
    
    @app.route('/marbres/<marbre_id>',methods=['DELETE'])
    def delete_marbre(marbre_id):
        marbre = Marbre.query.get(marbre_id)
        marbre.delete()
        return jsonify({
            'success': True,
            'deleted': marbre.format()
        })

    return app

app = create_app()

if __name__ == '__main__':
    app.run()

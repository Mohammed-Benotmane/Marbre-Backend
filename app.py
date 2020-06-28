import os
from flask import Flask,jsonify,request,abort
from models import setup_db
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

        try:
            marbre = Marbre(title = new_title,image= new_image, price=new_price, origin=new_origin)
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
    return app

app = create_app()

if __name__ == '__main__':
    app.run()

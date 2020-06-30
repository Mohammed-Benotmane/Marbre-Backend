from sqlalchemy import Column, String, create_engine,Integer,ForeignKey
from flask_sqlalchemy import SQLAlchemy
import json
import os
database_name="marbreproject"
database_path = os.environ.get('DATABASE_URL',"postgres://{}:{}@{}/{}".format('postgres', 'postgres','localhost:5432', database_name))

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

class Marbre(db.Model):
    id = Column(Integer(), primary_key=True)
    title = Column(String(80))
    image = Column(String(200))
    price = Column(Integer())
    origin = Column(String(80))
    description = Column(String(500))

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def format(self):
        return {
        'id': self.id,
        'title': self.title,
        'image': self.image,
        'price': self.price,
        'origin': self.origin,
        'description':self.description,
        }
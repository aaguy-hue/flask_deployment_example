from flask import Blueprint
from flask_restful import Api, Resource


skidoo_api = Blueprint('skidoo_api', __name__, url_prefix='/api/skidoo')
api = Api(skidoo_api)

class SkidooApi(Resource):
    def get(self):
        return {
            "title": "Origins of the term 23 skidoo", 
            "body": "The term 23 skidoo means to 'get out' and originated from the combination of the terms 23 and skidoo, which originated in 1899 and 1901 respectively.\nLearn more on the <a href='https://en.wikipedia.org/wiki/23_skidoo'>wikipedia page</a>."
        }



api.add_resource(SkidooApi, '/', '')

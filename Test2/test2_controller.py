from flask_restful import Resource, Api
from resources.Test2.test2_model import Test2 as test2_model
import json


model = test2_model

class Test2(Resource):
    def get(self):
        all_elements = model.objects.all()
        if not all_elements:
            all_elements = ['uno','dos','tres']
        else:
            all_elements = json.loads(all_elements.to_json())
        return {'data': all_elements}
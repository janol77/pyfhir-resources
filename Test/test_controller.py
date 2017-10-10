from flask_restful import Resource, Api
from resources.Test.test_model import Test as test_model
import json


model = test_model

class Test(Resource):
    def get(self):
        all_elements = model.objects.all()
        if not all_elements:
            all_elements = ['uno','dos','tres']
        else:
            all_elements = json.loads(all_elements.to_json())
        return {'data': all_elements}
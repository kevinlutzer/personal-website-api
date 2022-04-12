
from flask import Flask
from flask_restful import Api, Resource

from api.visitor import CreateVisitor

app = Flask(__name__)
api = Api(app)

class Health(Resource):
    def post(self):
        return {'hello': 'world'}

# Routes
api.add_resource(Health, '/')
api.add_resource(CreateVisitor, '/api/v1/createvisitor')

if __name__ == '__main__':
    app.run(debug=True)
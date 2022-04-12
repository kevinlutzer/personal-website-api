from flask import request
from flask_restful import Resource, Headers
from models import Visitor, Session

class CreateVisitor(Resource):
    def put(self):
        
        # Visitor.create()
        request.headers
        return {'result': request.headers}
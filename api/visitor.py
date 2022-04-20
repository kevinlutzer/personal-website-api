
from flask import request
from flask_restful import Resource
from models import Visitor, Session
from formencode import Schema, validators
from flask import current_app as app

class CreateVisitorPutSchema(Schema): 
    type = validators.OneOf(['professor'])

class CreateVisitor(Resource):

    def put(self):
        form = CreateVisitorPutSchema.to_python(request.json)

        with Session() as session:
            app.logger.info("CreateVisitor-PUT: Start")
            
            db = Visitor.create(request.headers.get("X-Forwarded-For"), form['type'])
            session.add(db)
            session.commit()

            app.logger.info("CreateVisitor-PUT: Created Visitor Successfully")

        return {
            "result": "successfully created the visitor"
        }
        
    
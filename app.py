import os
from flask import Flask, jsonify
from flask_restful import Api, Resource
from werkzeug.exceptions import HTTPException
from api.visitor import CreateVisitor
from formencode import Invalid

app = Flask(__name__)
api = Api(app)

if os.environ.get("SERVER_MODE") == "devel":
    @app.errorhandler(Exception)
    def handle_exception(e):
        # pass through HTTP errors
        if isinstance(e, HTTPException):
            return e

        return jsonify({
                'error': 'Server has encountered some error'
            }), 500

# Treat all formencode invalids as a precondition fail
@app.errorhandler(Invalid)
def handle_exception(e):
    return jsonify({
            'error': str(e)
        }), 412

class Health(Resource):
    def get(self):
        return {'result': 'alive'}

# Routes
api.add_resource(Health, '/health')
api.add_resource(CreateVisitor, '/api/v1/createvisitor')

if __name__ == '__main__':

    debug = True

    app.run(
        debug=debug,
        use_debugger=debug,
        use_reloader=debug,
        host='localhost'
    )
import os
from flask import Flask, jsonify
from flask_restful import Api
from werkzeug.exceptions import HTTPException
from api.health import Health
from api.visitor import CreateVisitor
from formencode import Invalid

from settings import API_MODE_DEV, DB_MODE_DEV

app = Flask(__name__)
api = Api(app)

if not DB_MODE_DEV:
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

# Routes
api.add_resource(Health, '/health')
api.add_resource(CreateVisitor, '/api/v1/createvisitor')

if __name__ == '__main__':

    # set host based on if we are doing local development
    host = '0.0.0.0'
    if API_MODE_DEV:
        host = 'localhost'

    app.logger.log(0, "Starting server")
    app.logger.log(0, "API Develement Dev Mode: {0}".format(API_MODE_DEV))
    app.logger.log(0, "DB Develement Dev Mode: {0}".format(DB_MODE_DEV))

    app.run(
        debug=API_MODE_DEV,
        use_debugger=API_MODE_DEV,
        use_reloader=API_MODE_DEV,
        host=host,
        port=5000
    )
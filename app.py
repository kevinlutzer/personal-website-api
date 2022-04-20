import os
from flask import Flask, jsonify
from flask_restful import Api, Resource
from werkzeug.exceptions import HTTPException
from api.health import Health
from api.visitor import CreateVisitor
from formencode import Invalid

app = Flask(__name__)
api = Api(app)

DEVEL = os.environ.get("SERVER_MODE") == 'dev'

if DEVEL:
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
    if DEVEL:
        host = 'localhost'

    app.logger.log(0, "starting server...")

    app.run(
        debug=DEVEL,
        use_debugger=DEVEL,
        use_reloader=DEVEL,
        host=host,
        port=5000
    )
from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, payload=None):
        Exception.__init__(self)
        self.message = message
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/recommender/', methods=['GET', 'POST'])
def add_message():
    content = request.get_json()
    if content is not None:
        doc = content.get('doc', {})
        docs = content.get('docs', [])
        if doc == {}:
            msg = 'The parameter `doc` is missing or empty'
            raise InvalidUsage(msg)
        if len(docs) == 0:
            msg = 'The parameter `docs` is missing or empty'
            raise InvalidUsage(msg)
        print(content, type(content), doc, docs, type(doc), type(docs))
    else:
        msg = 'You need to send the parameters: doc and docs'
        raise InvalidUsage(msg)
    return 'uuid'
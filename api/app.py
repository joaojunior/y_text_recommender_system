from flask import Flask
from flask import request
from flask import jsonify

from y_text_recommender_system.recommender import recommend

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


@app.route('/recommender/', methods=['POST'])
def recommender():
    content = request.get_json()
    if content is not None:
        doc = content.get('doc', {})
        docs = content.get('docs', [])
        _verify_parameters(doc, docs)
        result = recommend(doc, docs)
        return jsonify(result)
    else:
        msg = 'You need to send the parameters: doc and docs'
        raise InvalidUsage(msg)


def _verify_parameters(doc, docs):
    if doc == {}:
        msg = 'The parameter `doc` is missing or empty'
        raise InvalidUsage(msg)
    if not isinstance(doc, dict):
        msg = 'The parameter `doc` should be a dict'
        raise InvalidUsage(msg)
    if len(docs) == 0:
        msg = 'The parameter `docs` is missing or empty'
        raise InvalidUsage(msg)

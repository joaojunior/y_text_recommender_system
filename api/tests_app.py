import unittest
import json

from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.url = '/recommender/'

    def test_post_without_parameters(self):
        rv = self.app.post(self.url)
        self.assertEqual(400, rv.status_code)
        expected = {'message': 'You need to send the parameters: doc and docs'}
        self.assertEqual(expected,
                         json.loads(rv.data.decode('utf-8')))

    def test_post_without_doc(self):
        docs = {'docs': [{'key1': 'value1'}]}
        data = json.dumps(docs)
        rv = self.app.post(self.url,
                           data=data, content_type='application/json')
        self.assertEqual(400, rv.status_code)
        expected = {'message': 'The parameter `doc` is missing or empty'}
        self.assertEqual(expected,
                         json.loads(rv.data.decode('utf-8')))

    def test_post_without_docs(self):
        doc = {'doc': {'key1': 'value1'}}
        data = json.dumps(doc)
        rv = self.app.post(self.url,
                           data=data, content_type='application/json')
        self.assertEqual(400, rv.status_code)
        expected = {'message': 'The parameter `docs` is missing or empty'}
        self.assertEqual(expected,
                         json.loads(rv.data.decode('utf-8')))

    def test_post_with_doc_empty(self):
        data = {'doc': {},
                'docs': [{'key1': 'value1'}]}
        data = json.dumps(data)
        rv = self.app.post(self.url,
                           data=data, content_type='application/json')
        self.assertEqual(400, rv.status_code)
        expected = {'message': 'The parameter `doc` is missing or empty'}
        self.assertEqual(expected,
                         json.loads(rv.data.decode('utf-8')))
if __name__ == '__main__':
    unittest.main()

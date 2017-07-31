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

    def test_post_with_docs_empty(self):
        data = {'doc': {'key1': 'value1'},
                'docs': []}
        data = json.dumps(data)
        rv = self.app.post(self.url,
                           data=data, content_type='application/json')
        self.assertEqual(400, rv.status_code)
        expected = {'message': 'The parameter `docs` is missing or empty'}
        self.assertEqual(expected,
                         json.loads(rv.data.decode('utf-8')))

    def test_post_with_parameters_are_correct(self):
        data = {'doc': {'key1': 'value1'},
                'docs': [{'doc1': 'value1'},
                         {'doc2': 'value1'}]}
        data = json.dumps(data)
        rv = self.app.post(self.url,
                           data=data, content_type='application/json')
        expected = [[1.0, {'doc1': 'value1'}], [1.0, {'doc2': 'value1'}]]
        actual = json.loads(rv.data.decode('utf-8'))
        self.assertEqual(200, rv.status_code)
        self.assertEqual(expected, actual)

    def test_post_with_doc_is_not_dict(self):
        data = {'doc': 'a',
                'docs': [{'doc1': 'value1'},
                         {'doc2': 'value1'}]}
        data = json.dumps(data)
        rv = self.app.post(self.url,
                           data=data, content_type='application/json')
        expected = {'message': 'The parameter `doc` should be a dict'}
        self.assertEqual(400, rv.status_code)
        self.assertEqual(expected, json.loads(rv.data.decode('utf-8')))

    def test_post_with_docs_is_not_list(self):
        data = {'doc': {'key1': 'value1'},
                'docs': {'doc1': 'value1'}}
        data = json.dumps(data)
        rv = self.app.post(self.url,
                           data=data, content_type='application/json')
        expected = {'message': 'The parameter `docs` should be a list of dict'}
        self.assertEqual(400, rv.status_code)
        self.assertEqual(expected, json.loads(rv.data.decode('utf-8')))

    def test_post_with_docs_is_not_list_of_dict(self):
        data = {'doc': {'key1': 'value1'},
                'docs': [{'a': 'b'}, 'a']}
        data = json.dumps(data)
        rv = self.app.post(self.url,
                           data=data, content_type='application/json')
        expected = {'message': 'The parameter `docs` should be a list of dict'}
        self.assertEqual(400, rv.status_code)
        self.assertEqual(expected, json.loads(rv.data.decode('utf-8')))

if __name__ == '__main__':
    unittest.main()

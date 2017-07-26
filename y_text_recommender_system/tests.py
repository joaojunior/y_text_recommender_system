import unittest

from recommender import recommend


def _extract_only_docs_from_result(result):
    return [doc for value, doc in result]


class TestRecommender(unittest.TestCase):
    def test_verify_recomender_same_doc(self):
        doc = {'doc': 'simple doc'}
        docs = [doc]
        expected = [doc]
        actual = recommend(doc, docs)
        actual = _extract_only_docs_from_result(actual)
        self.assertEqual(expected, actual)

    def test_verify_recommender_docs_one_word(self):
        doc = {'doc1': 'one'}
        docs = [{'doc3': 'one two three'},
                {'doc2': 'one two'}]
        expected = [{'doc2': 'one two'},
                    {'doc3': 'one two three'}]
        actual = recommend(doc, docs)
        actual = _extract_only_docs_from_result(actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

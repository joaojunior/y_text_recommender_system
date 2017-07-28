import unittest

from y_text_recommender_system.recommender import recommend


def _extract_only_docs_from_result(result):
    return [doc for value, doc in result]


class TestRecommender(unittest.TestCase):
    def test_recommender_same_doc(self):
        doc = {'doc': 'simple doc'}
        docs = [doc]
        expected = [doc]
        actual = recommend(doc, docs)
        actual = _extract_only_docs_from_result(actual)
        self.assertEqual(expected, actual)

    def test_recommender_docs_one_word_in_common(self):
        doc = {'doc1': 'one'}
        docs = [{'doc3': 'one two three'},
                {'doc2': 'one two'}]
        expected = [{'doc2': 'one two'},
                    {'doc3': 'one two three'}]
        actual = recommend(doc, docs)
        actual = _extract_only_docs_from_result(actual)
        self.assertEqual(expected, actual)

    def test_recommender_none_word_in_common(self):
        doc = {'doc1': 'zero'}
        docs = [{'doc3': 'one two three'},
                {'doc2': 'one two'}]
        expected = [(0.0, {'doc3': 'one two three'}),
                    (0.0, {'doc2': 'one two'})]
        actual = recommend(doc, docs)
        self.assertEqual(expected, actual)


class TestRecommenderSystemWithStopWords(unittest.TestCase):
    def setUp(self):
        self.doc = {'doc1': 'one two two three'}
        self.docs = [{'doc2': 'one two two'},
                     {'doc3': 'one three'}]

    def test_verify_recommender_without_stop_words(self):
        expected = [{'doc2': 'one two two'},
                    {'doc3': 'one three'}]
        actual = recommend(self.doc, self.docs)
        actual = _extract_only_docs_from_result(actual)
        self.assertEqual(expected, actual)

    def test_verify_recommender_with_stop_words(self):
        expected = [{'doc3': 'one three'},
                    {'doc2': 'one two two'}]
        actual = recommend(self.doc, self.docs, stop_words=['two'])
        actual = _extract_only_docs_from_result(actual)
        self.assertEqual(expected, actual)


class TestRecommenderDictMultipleKeys(unittest.TestCase):
    def test_recommender_dict_with_two_keys(self):
        docs = [{'key1': 'not', 'key2': 'equal'},
                {'key1': 'word1', 'key2': 'word2'}]
        doc = {'key': 'word2', 'key3': 'word3'}
        expected = [{'key1': 'word1', 'key2': 'word2'},
                    {'key1': 'not', 'key2': 'equal'}]
        actual = recommend(doc, docs)
        self.assertNotEqual(0, actual[0][0])
        self.assertEqual(0, actual[1][0])
        actual = _extract_only_docs_from_result(actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

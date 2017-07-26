import unittest

from recommender import recommend


class TestRecommender(unittest.TestCase):
    def test_verify_recomender_same_doc(self):
        doc = {'doc': 'simple doc'}
        docs = [doc]
        expected = doc
        self.assertEqual(expected, recommend(doc, docs)[0][1])


if __name__ == '__main__':
    unittest.main()

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def recommend(doc, docs):
    vectorizer = TfidfVectorizer(min_df=1)
    docs.insert(0, doc)
    corpus = create_corpus_from_dict(docs)
    model = vectorizer.fit_transform(corpus)
    model_dense = model.todense()
    similarity = calculate_similarity(model_dense)
    docs.pop(0)
    return sorted(zip(similarity, docs), reverse=True)


def create_corpus_from_dict(docs):
    corpus = []
    for doc in docs:
        for key, value in doc.items():
            corpus.append(value)
    return corpus


def calculate_similarity(model_dense):
    similarity = []
    tfidf_main_doc = model_dense[0, :]
    for tfidf_doc in model_dense[1, :]:
        similarity.append(cosine_sim(tfidf_main_doc, tfidf_doc.T))
    return similarity


def cosine_sim(vec1, vec2):
    return np.dot(vec1, vec2)[0, 0]

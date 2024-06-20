import numpy as np

import oldv

from .document_vectorizers.fixtures import all_minilm_hello_world_vector


def test_oldv_as_module_vectorize() -> None:
    document_vectorizer = oldv.AllMiniLmVectorizer.create()
    dv = oldv.DocumentVectorizerCore(document_vectorizer)
    res = dv.vectorize(oldv.Document(content=oldv.DocumentContent("Hello world")))
    assert isinstance(res, oldv.DocumentVector)
    assert np.allclose(res.vector.array, all_minilm_hello_world_vector)

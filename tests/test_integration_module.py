import numpy as np

import oldv

from .document_vectorizers.fixtures import all_minilm_hello_world_vector


def test_oldv_as_module_vectorize() -> None:
    core = oldv.AllMiniLmVectorizerCore.create()
    dv = oldv.DocumentVectorizerApp(core)
    res = dv.vectorize(oldv.Document(content=oldv.DocumentContent("Hello world")))
    assert isinstance(res, oldv.DocumentVector)
    assert np.allclose(res.vector.array, all_minilm_hello_world_vector)

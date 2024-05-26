import numpy as np

from oldv.document_vectorizers.all_minilm import AllMiniLmVectorizerCore
from oldv.models import Document

from .fixtures import all_minilm_hello_world_vector


def test_all_minilm() -> None:
    expected = all_minilm_hello_world_vector
    core = AllMiniLmVectorizerCore.create()
    assert np.allclose(core.vectorize(Document(content="Hello World")).vector.array, expected, atol=1e-6)

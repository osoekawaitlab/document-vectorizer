import numpy as np

from oldv.document_vectorizers.all_minilm import AllMiniLmVectorizerCore
from oldv.models import Document

from .fixtures import all_minilm_hello_computer_vector, all_minilm_hello_world_vector


def test_all_minilm_vectorize() -> None:
    expected = all_minilm_hello_world_vector
    core = AllMiniLmVectorizerCore.create()
    assert np.allclose(core.vectorize(Document(content="Hello World")).vector.array, expected, atol=1e-6)


def test_all_minilm_batch_vectorize() -> None:
    expected = [all_minilm_hello_world_vector, all_minilm_hello_computer_vector]
    core = AllMiniLmVectorizerCore.create()
    cnt = 0
    for a, e in zip(
        core.batch_vectorize([Document(content="Hello World"), Document(content="Hello Computer")]), expected
    ):
        assert np.allclose(a.vector.array, e, atol=1e-6)
        cnt += 1
    assert cnt == 2

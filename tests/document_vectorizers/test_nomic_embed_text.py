import numpy as np

from oldv.document_vectorizers.nomic_embed_text import NomicEmbedTextCore
from oldv.models import Document

from .fixtures import (
    nomic_embed_text_hello_computer_vector,
    nomic_embed_text_hello_world_vector,
)


def test_nomic_embed_text_core() -> None:
    expected = nomic_embed_text_hello_world_vector
    sut = NomicEmbedTextCore.create()
    assert np.allclose(sut.vectorize(Document(content="Hello World")).vector.array, expected, atol=1e-5)


def test_monic_embed_supports_batch_vectorization() -> None:
    expected = [nomic_embed_text_hello_world_vector, nomic_embed_text_hello_computer_vector]
    sut = NomicEmbedTextCore.create()
    cnt = 0
    for a, e in zip(
        sut.batch_vectorize([Document(content="Hello World"), Document(content="Hello Computer")]), expected
    ):
        cnt += 1
        assert np.allclose(a.vector.array, e, atol=1e-5)
    assert cnt == 2

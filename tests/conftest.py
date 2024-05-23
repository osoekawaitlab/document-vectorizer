from unittest.mock import MagicMock

from pytest import fixture

from oldv.document_vectorizers.base import BaseDocumentVectorizerCore


@fixture
def mock_vectorizer_core() -> MagicMock:
    return MagicMock(spec=BaseDocumentVectorizerCore)

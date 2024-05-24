from unittest.mock import MagicMock

from pytest import fixture

from oldv.document_vectorizers.base import (
    BaseDocumentVectorizerCore,
    SupportsBatchVectorizationMixIn,
)


@fixture
def mock_vectorizer_core() -> MagicMock:
    return MagicMock(spec=BaseDocumentVectorizerCore)


@fixture
def mock_vectorizer_core_supports_batch() -> MagicMock:
    return MagicMock(spec=SupportsBatchVectorizationMixIn)

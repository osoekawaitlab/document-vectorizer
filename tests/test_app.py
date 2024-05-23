from unittest.mock import MagicMock

from oldv.app import DocumentVectorizerApp
from oldv.models import Document


def test_vectorize(mock_vectorizer_core: MagicMock) -> None:
    dv = DocumentVectorizerApp(core=mock_vectorizer_core)
    res = dv.vectorize(Document(content="Hello world"))
    assert res == mock_vectorizer_core.vectorize.return_value
    mock_vectorizer_core.vectorize.assert_called_once_with(Document(content="Hello world"))

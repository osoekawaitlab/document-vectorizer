from unittest.mock import MagicMock, call

from oldv.app import DocumentVectorizerApp
from oldv.models import Document


def test_vectorize(mock_vectorizer_core: MagicMock) -> None:
    sut = DocumentVectorizerApp(core=mock_vectorizer_core)
    res = sut.vectorize(Document(content="Hello world"))
    assert res == mock_vectorizer_core.vectorize.return_value
    mock_vectorizer_core.vectorize.assert_called_once_with(Document(content="Hello world"))


def test_batch_vectorize_with_unsupported_core(mock_vectorizer_core: MagicMock) -> None:
    sut = DocumentVectorizerApp(core=mock_vectorizer_core)
    res = sut.batch_vectorize([Document(content="Hello world"), Document(content="Good night world")])
    assert res == [mock_vectorizer_core.vectorize.return_value, mock_vectorizer_core.vectorize.return_value]
    mock_vectorizer_core.vectorize.assert_has_calls(
        [call(Document(content="Hello world")), call(Document(content="Good night world"))]
    )


def test_batch_vectorize_with_supported_core(mock_vectorizer_core_supports_batch: MagicMock) -> None:
    sut = DocumentVectorizerApp(core=mock_vectorizer_core_supports_batch)
    arg = [Document(content="Hello world"), Document(content="Good night world")]
    res = sut.batch_vectorize(arg)
    assert res == mock_vectorizer_core_supports_batch.batch_vectorize.return_value
    mock_vectorizer_core_supports_batch.batch_vectorize.assert_called_once_with(arg)
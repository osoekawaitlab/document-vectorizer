from unittest.mock import MagicMock, call

from oldv.app import DocumentVectorizerApp
from oldv.models import Document
from oldv.settings import (
    AllMiniLmDocumentVectorizerSettings,
    DocumentVectorizerAppSettings,
)


def test_vectorize(mock_vectorizer: MagicMock) -> None:
    sut = DocumentVectorizerApp(document_vectorizer=mock_vectorizer)
    res = sut.vectorize(Document(content="Hello world"))
    assert res == mock_vectorizer.vectorize.return_value
    mock_vectorizer.vectorize.assert_called_once_with(Document(content="Hello world"))


def test_batch_vectorize_with_unsupported_document_vectorizer(mock_vectorizer: MagicMock) -> None:
    sut = DocumentVectorizerApp(document_vectorizer=mock_vectorizer)
    res = sut.batch_vectorize([Document(content="Hello world"), Document(content="Good night world")])
    assert res == [mock_vectorizer.vectorize.return_value, mock_vectorizer.vectorize.return_value]
    mock_vectorizer.vectorize.assert_has_calls(
        [call(Document(content="Hello world")), call(Document(content="Good night world"))]
    )


def test_batch_vectorize_with_supported_document_vectorizer(mock_vectorizer_supports_batch: MagicMock) -> None:
    sut = DocumentVectorizerApp(document_vectorizer=mock_vectorizer_supports_batch)
    arg = [Document(content="Hello world"), Document(content="Good night world")]
    res = sut.batch_vectorize(arg)
    assert res == mock_vectorizer_supports_batch.batch_vectorize.return_value
    mock_vectorizer_supports_batch.batch_vectorize.assert_called_once_with(arg)


def test_create(mocker: MagicMock, mock_vectorizer: MagicMock) -> None:
    create_document_vectorizer = mocker.patch("oldv.app.create_document_vectorizer", return_value=mock_vectorizer)
    settings = DocumentVectorizerAppSettings(document_vectorizer_settings=AllMiniLmDocumentVectorizerSettings())
    actual = DocumentVectorizerApp.create(settings=settings)
    assert actual.document_vectorizer == mock_vectorizer
    create_document_vectorizer.assert_called_once_with(settings=settings.document_vectorizer_settings)

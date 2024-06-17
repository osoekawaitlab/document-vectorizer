from pytest_mock import MockerFixture

from oldv.document_vectorizers.factory import create_document_vectorizer
from oldv.settings import (
    AllMiniLmDocumentVectorizerSettings,
    NomicEmbedTextDocumentVectorizerSettings,
)


def test_create_all_minilm_document_vectorizer(mocker: MockerFixture) -> None:
    AllMiniLmVectorizer = mocker.patch("oldv.document_vectorizers.factory.AllMiniLmVectorizer")
    actual = create_document_vectorizer(settings=AllMiniLmDocumentVectorizerSettings())
    AllMiniLmVectorizer.create.assert_called_once_with()
    assert actual == AllMiniLmVectorizer.create.return_value


def test_create_nomic_embed_text_document_vectorizer(mocker: MockerFixture) -> None:
    NomicEmbedTextVectorizer = mocker.patch("oldv.document_vectorizers.factory.NomicEmbedTextVectorizer")
    actual = create_document_vectorizer(settings=NomicEmbedTextDocumentVectorizerSettings())
    NomicEmbedTextVectorizer.create.assert_called_once_with()
    assert actual == NomicEmbedTextVectorizer.create.return_value

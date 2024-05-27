from pytest_mock import MockerFixture

from oldv.document_vectorizers.factory import create_document_vectorizer_core
from oldv.settings import AllMiniLmDocumentVectorizerCoreSettings


def test_create_all_minilm_document_vectorizer_core(mocker: MockerFixture) -> None:
    AllMiniLmVectorizerCore = mocker.patch("oldv.document_vectorizers.factory.AllMiniLmVectorizerCore")
    actual = create_document_vectorizer_core(settings=AllMiniLmDocumentVectorizerCoreSettings())
    AllMiniLmVectorizerCore.create.assert_called_once_with()
    assert actual == AllMiniLmVectorizerCore.create.return_value

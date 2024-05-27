from collections.abc import Generator
from unittest.mock import MagicMock

from pytest import fixture
from pytest_mock import MockerFixture

from oldv.app import DocumentVectorizerApp
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


@fixture
def mock_document_vectorizer_app() -> MagicMock:
    return MagicMock(spec=DocumentVectorizerApp)


@fixture
def patch_empty_environment_variables(mocker: MockerFixture) -> Generator[None, None, None]:
    mocker.patch("os.environ", {})
    yield


@fixture
def patch_all_minilm_environment_variable(
    patch_empty_environment_variables: None, mocker: MockerFixture
) -> Generator[None, None, None]:
    mocker.patch("os.environ", {"OLDV_DOCUMENT_VECTORIZER__TYPE": "ALL_MINI_LM"})
    yield

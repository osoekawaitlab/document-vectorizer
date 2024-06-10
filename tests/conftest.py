import os
from collections.abc import Generator
from unittest.mock import MagicMock

from fastapi.testclient import TestClient
from pytest import fixture
from pytest_mock import MockerFixture

from oldv.app import DocumentVectorizerApp
from oldv.document_vectorizers.base import (
    BaseDocumentVectorizerCore,
    SupportsBatchVectorizationMixIn,
)
from oldv.interfaces.api.app import gen_api_app


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
    current_environment_variables = os.environ.copy()
    mocker.patch("os.environ", {k: v for k, v in current_environment_variables.items() if not k.startswith("OLDV_")})
    yield


@fixture
def patch_all_minilm_environment_variable(
    patch_empty_environment_variables: None, mocker: MockerFixture
) -> Generator[None, None, None]:
    mocker.patch("os.environ", dict(os.environ, OLDV_DOCUMENT_VECTORIZER_CORE_SETTINGS__TYPE="ALL_MINI_LM"))
    yield


@fixture
def api_app_client(patch_all_minilm_environment_variable: None) -> Generator[TestClient, None, None]:
    app = gen_api_app()
    with TestClient(app) as client:
        yield client

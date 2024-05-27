from ..settings import (
    AllMiniLmDocumentVectorizerCoreSettings,
    DocumentVectorizerCoreSettings,
)
from .all_minilm import AllMiniLmVectorizerCore
from .base import BaseDocumentVectorizerCore


def create_document_vectorizer_core(settings: DocumentVectorizerCoreSettings) -> BaseDocumentVectorizerCore:
    if isinstance(settings, AllMiniLmDocumentVectorizerCoreSettings):
        return AllMiniLmVectorizerCore.create()
    raise NotImplementedError()

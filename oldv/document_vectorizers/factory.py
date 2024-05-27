from ..settings import AllMiniLmVectorizerCoreSettings, DocumentVectorizerSettings
from .all_minilm import AllMiniLmVectorizerCore
from .base import BaseDocumentVectorizerCore


def create_document_vectorizer_core(settings: DocumentVectorizerSettings) -> BaseDocumentVectorizerCore:
    if isinstance(settings, AllMiniLmVectorizerCoreSettings):
        return AllMiniLmVectorizerCore.create()
    raise NotImplementedError()

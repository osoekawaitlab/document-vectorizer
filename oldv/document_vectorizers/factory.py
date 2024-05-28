from ..settings import (
    AllMiniLmDocumentVectorizerCoreSettings,
    DocumentVectorizerCoreSettings,
    NomicEmbedTextDocumentVectorizerCoreSettings,
)
from .all_minilm import AllMiniLmVectorizerCore
from .base import BaseDocumentVectorizerCore
from .nomic_embed_text import NomicEmbedTextVectorizerCore


def create_document_vectorizer_core(settings: DocumentVectorizerCoreSettings) -> BaseDocumentVectorizerCore:
    if isinstance(settings, AllMiniLmDocumentVectorizerCoreSettings):
        return AllMiniLmVectorizerCore.create()
    elif isinstance(settings, NomicEmbedTextDocumentVectorizerCoreSettings):
        return NomicEmbedTextVectorizerCore.create()
    raise NotImplementedError()

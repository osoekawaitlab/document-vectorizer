from ..settings import (
    AllMiniLmDocumentVectorizerModelSettings,
    DocumentVectorizerModelSettings,
    NomicEmbedTextDocumentVectorizerModelSettings,
)
from .all_minilm import AllMiniLmVectorizer
from .base import BaseDocumentVectorizer
from .nomic_embed_text import NomicEmbedTextVectorizer


def create_document_vectorizer(settings: DocumentVectorizerModelSettings) -> BaseDocumentVectorizer:
    if isinstance(settings, AllMiniLmDocumentVectorizerModelSettings):
        return AllMiniLmVectorizer.create()
    elif isinstance(settings, NomicEmbedTextDocumentVectorizerModelSettings):
        return NomicEmbedTextVectorizer.create()
    raise NotImplementedError()

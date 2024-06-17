from ..settings import (
    AllMiniLmDocumentVectorizerSettings,
    DocumentVectorizerSettings,
    NomicEmbedTextDocumentVectorizerSettings,
)
from .all_minilm import AllMiniLmVectorizer
from .base import BaseDocumentVectorizer
from .nomic_embed_text import NomicEmbedTextVectorizer


def create_document_vectorizer(settings: DocumentVectorizerSettings) -> BaseDocumentVectorizer:
    if isinstance(settings, AllMiniLmDocumentVectorizerSettings):
        return AllMiniLmVectorizer.create()
    elif isinstance(settings, NomicEmbedTextDocumentVectorizerSettings):
        return NomicEmbedTextVectorizer.create()
    raise NotImplementedError()

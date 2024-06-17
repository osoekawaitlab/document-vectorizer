from collections.abc import Sequence

from .document_vectorizers.base import (
    BaseDocumentVectorizer,
    SupportsBatchVectorizationMixIn,
)
from .document_vectorizers.factory import create_document_vectorizer
from .models import Document, DocumentVector
from .settings import DocumentVectorizerAppSettings


class DocumentVectorizerApp:
    def __init__(self, document_vectorizer: BaseDocumentVectorizer):
        self._document_vectorizer = document_vectorizer

    @property
    def document_vectorizer(self) -> BaseDocumentVectorizer:
        return self._document_vectorizer

    def vectorize(self, doc: Document) -> DocumentVector:
        return self.document_vectorizer.vectorize(doc)

    def batch_vectorize(self, docs: Sequence[Document]) -> Sequence[DocumentVector]:
        if isinstance(self.document_vectorizer, SupportsBatchVectorizationMixIn):
            return self.document_vectorizer.batch_vectorize(docs)
        return [self.vectorize(doc) for doc in docs]

    @classmethod
    def create(cls, settings: DocumentVectorizerAppSettings) -> "DocumentVectorizerApp":
        return cls(document_vectorizer=create_document_vectorizer(settings=settings.document_vectorizer_settings))

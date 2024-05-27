from collections.abc import Sequence

from .document_vectorizers.base import (
    BaseDocumentVectorizerCore,
    SupportsBatchVectorizationMixIn,
)
from .models import Document, DocumentVector
from .settings import DocumentVectorizerAppSettings


class DocumentVectorizerApp:
    def __init__(self, core: BaseDocumentVectorizerCore):
        self._core = core

    @property
    def core(self) -> BaseDocumentVectorizerCore:
        return self._core

    def vectorize(self, doc: Document) -> DocumentVector:
        return self.core.vectorize(doc)

    def batch_vectorize(self, docs: Sequence[Document]) -> Sequence[DocumentVector]:
        if isinstance(self.core, SupportsBatchVectorizationMixIn):
            return self.core.batch_vectorize(docs)
        return [self.vectorize(doc) for doc in docs]

    @classmethod
    def create(cls, settings: DocumentVectorizerAppSettings) -> "DocumentVectorizerApp": ...

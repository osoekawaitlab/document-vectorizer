from .document_vectorizers.base import BaseDocumentVectorizerCore
from .models import Document, DocumentVector


class DocumentVectorizerApp:
    def __init__(self, core: BaseDocumentVectorizerCore):
        self._core = core

    @property
    def core(self) -> BaseDocumentVectorizerCore:
        return self._core

    def vectorize(self, doc: Document) -> DocumentVector:
        return self.core.vectorize(doc)

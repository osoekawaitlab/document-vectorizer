from .document_vectorizers.base import BaseDocumentVectorizerCore
from .types import DocumentContent, Vector


class DocumentVectorizerApp:
    def __init__(self, core: BaseDocumentVectorizerCore):
        self._core = core

    @property
    def core(self) -> BaseDocumentVectorizerCore:
        return self._core

    def vectorize(self, text: DocumentContent) -> Vector:
        return self.core.vectorize(text)

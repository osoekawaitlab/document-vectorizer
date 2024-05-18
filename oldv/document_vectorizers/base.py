from abc import ABC, abstractmethod

from ..models import Document, DocumentVector


class BaseDocumentVectorizerCore(ABC):
    @abstractmethod
    def vectorize(self, doc: Document) -> DocumentVector: ...

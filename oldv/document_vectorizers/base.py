from abc import ABC, abstractmethod

from ..types import DocumentContent, Vector


class BaseDocumentVectorizerCore(ABC):
    @abstractmethod
    def vectorize(self, text: DocumentContent) -> Vector: ...

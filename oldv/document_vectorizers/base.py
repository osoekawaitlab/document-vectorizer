from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Generic, Type, TypeVar

from ..models import BaseModel, Document, DocumentVector
from ..types import PickleBytes

DocumentVectorizerT = TypeVar("DocumentVectorizerT", bound="BaseDocumentVectorizer")
SerializedDocumentVectorizerT = TypeVar("SerializedDocumentVectorizerT", bound="BaseSerializedDocumentVectorizer")


class BaseDocumentVectorizer(ABC):
    @abstractmethod
    def vectorize(self, doc: Document) -> DocumentVector: ...


class BaseSerializedDocumentVectorizer(BaseModel):
    serialized_document_vectorizer: PickleBytes


class SupportsSerializationMixIn(BaseDocumentVectorizer, Generic[SerializedDocumentVectorizerT]):
    @abstractmethod
    def serialize(self) -> SerializedDocumentVectorizerT: ...

    @classmethod
    @abstractmethod
    def deserialize(cls: Type[DocumentVectorizerT], s: SerializedDocumentVectorizerT) -> DocumentVectorizerT: ...


class SupportsBatchVectorizationMixIn(BaseDocumentVectorizer):
    @abstractmethod
    def batch_vectorize(self, docs: Sequence[Document]) -> Sequence[DocumentVector]: ...

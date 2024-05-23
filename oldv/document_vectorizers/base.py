from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Generic, Type, TypeVar

from ..models import BaseModel, Document, DocumentVector
from ..types import PickleBytes

DocumentVectorizerCoreT = TypeVar("DocumentVectorizerCoreT", bound="BaseDocumentVectorizerCore")
SerializedDocumentVectorizerCoreT = TypeVar(
    "SerializedDocumentVectorizerCoreT", bound="BaseSerializedDocumentVectorizer"
)


class BaseDocumentVectorizerCore(ABC):
    @abstractmethod
    def vectorize(self, doc: Document) -> DocumentVector: ...


class BaseSerializedDocumentVectorizer(BaseModel):
    serialized_document_vectorizer: PickleBytes


class SupportsSerializationMixIn(BaseDocumentVectorizerCore, Generic[SerializedDocumentVectorizerCoreT]):
    @abstractmethod
    def serialize(self) -> SerializedDocumentVectorizerCoreT: ...

    @classmethod
    @abstractmethod
    def deserialize(
        cls: Type[DocumentVectorizerCoreT], s: SerializedDocumentVectorizerCoreT
    ) -> DocumentVectorizerCoreT: ...


class SupportsBatchVectorizationMixIn(BaseDocumentVectorizerCore):
    @abstractmethod
    def batch_vectorize(self, docs: Sequence[Document]) -> Sequence[DocumentVector]: ...

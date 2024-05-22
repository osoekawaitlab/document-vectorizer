import pickle
from collections.abc import Sequence

from sklearn.feature_extraction.text import CountVectorizer

from ..models import Document, DocumentVector
from ..settings import CountVectorizerSettings
from ..types import PickleBytes, Scalar, Vector
from .base import BaseSerializedDocumentVectorizer, SupportsSerializationMixIn


class SerializedCountVectorizer(BaseSerializedDocumentVectorizer): ...


class CountVectorizerCore(SupportsSerializationMixIn[SerializedCountVectorizer]):
    def __init__(self, count_vectorizer: CountVectorizer):
        super(CountVectorizerCore, self).__init__()
        self._count_vectorizer = count_vectorizer

    @property
    def count_vectorizer(self) -> CountVectorizer:
        return self._count_vectorizer

    def vectorize(self, doc: Document) -> DocumentVector:
        x = self.count_vectorizer.transform([doc.content])
        return DocumentVector(vector=Vector.from_array(x.toarray()[0]))

    @classmethod
    def create(cls, corpus: Sequence[Document], settings: CountVectorizerSettings) -> "CountVectorizerCore":
        count_vectorizer = CountVectorizer(analyzer=settings.analyzer.lower(), dtype=Scalar)
        count_vectorizer.fit([d.content for d in corpus])
        return cls(count_vectorizer=count_vectorizer)

    def serialize(self) -> SerializedCountVectorizer:
        return SerializedCountVectorizer(
            serialized_document_vectorizer=PickleBytes(pickle.dumps(self.count_vectorizer))
        )

    @classmethod
    def deserialize(cls, s: SerializedCountVectorizer) -> "CountVectorizerCore":
        count_vectorizer = pickle.loads(s.serialized_document_vectorizer)
        return cls(count_vectorizer=count_vectorizer)

import pickle
from collections.abc import Sequence

from sklearn.feature_extraction.text import CountVectorizer

from ..models import BaseModel, Document, DocumentVector
from ..settings import CountVectorizerSettings
from ..types import PickleBytes, Scalar, Vector
from .base import BaseDocumentVectorizerCore


class SerializedCountVectorizer(BaseModel):
    serialized_count_vectorizer: PickleBytes


class CountVectorizerCore(BaseDocumentVectorizerCore):
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
        return SerializedCountVectorizer(serialized_count_vectorizer=PickleBytes(pickle.dumps(self.count_vectorizer)))

    @classmethod
    def deserialize(cls, serialized: SerializedCountVectorizer) -> "CountVectorizerCore":
        count_vectorizer = pickle.loads(serialized.serialized_count_vectorizer)
        return cls(count_vectorizer=count_vectorizer)

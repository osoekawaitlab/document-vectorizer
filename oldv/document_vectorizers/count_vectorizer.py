from collections.abc import Sequence

from sklearn.feature_extraction.text import CountVectorizer

from ..settings import CountVectorizerSettings
from ..types import DocumentContent, Scalar, Vector
from .base import BaseDocumentVectorizerCore


class CountVectorizerCore(BaseDocumentVectorizerCore):
    def __init__(self, count_vectorizer: CountVectorizer):
        super(CountVectorizerCore, self).__init__()
        self._count_vectorizer = count_vectorizer

    @property
    def count_vectorizer(self) -> CountVectorizer:
        return self._count_vectorizer

    def vectorize(self, text: DocumentContent) -> Vector:
        x = self.count_vectorizer.transform([text])
        return Vector.from_array(x.toarray()[0])

    @classmethod
    def create(cls, corpus: Sequence[DocumentContent], settings: CountVectorizerSettings) -> "CountVectorizerCore":
        count_vectorizer = CountVectorizer(analyzer=settings.analyzer.lower(), dtype=Scalar)
        count_vectorizer.fit(corpus)
        return cls(count_vectorizer=count_vectorizer)

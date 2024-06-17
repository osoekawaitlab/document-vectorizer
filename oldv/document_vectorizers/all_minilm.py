from typing import Sequence

from sentence_transformers import SentenceTransformer

from ..models import Document, DocumentVector
from ..types import Vector
from .base import SupportsBatchVectorizationMixIn


class AllMiniLmVectorizer(SupportsBatchVectorizationMixIn):
    def __init__(self, model: SentenceTransformer):
        super(AllMiniLmVectorizer, self).__init__()
        self._model = model

    def vectorize(self, doc: Document) -> DocumentVector:
        return DocumentVector(vector=Vector.from_array(self._model.encode([doc.content])[0]))

    @classmethod
    def create(cls) -> "AllMiniLmVectorizer":
        return cls(SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2"))

    def batch_vectorize(self, docs: Sequence[Document]) -> Sequence[DocumentVector]:
        return [DocumentVector(vector=Vector.from_array(v)) for v in self._model.encode([doc.content for doc in docs])]

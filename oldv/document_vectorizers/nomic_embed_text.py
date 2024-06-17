from typing import Sequence

from sentence_transformers import SentenceTransformer

from ..models import Document, DocumentVector
from ..types import Vector
from .base import SupportsBatchVectorizationMixIn


class NomicEmbedTextVectorizer(SupportsBatchVectorizationMixIn):
    def __init__(self, model: SentenceTransformer):
        super(NomicEmbedTextVectorizer, self).__init__()
        self._model = model

    def vectorize(self, doc: Document) -> DocumentVector:
        return DocumentVector(vector=Vector.from_array(self._model.encode([doc.content])[0]))

    @classmethod
    def create(cls) -> "NomicEmbedTextVectorizer":
        return cls(SentenceTransformer("nomic-ai/nomic-embed-text-v1.5", trust_remote_code=True))

    def batch_vectorize(self, docs: Sequence[Document]) -> Sequence[DocumentVector]:
        arr = self._model.encode([doc.content for doc in docs])
        return [DocumentVector(vector=Vector.from_array(v)) for v in arr]

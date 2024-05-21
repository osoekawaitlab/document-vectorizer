from sentence_transformers import SentenceTransformer

from ..models import Document, DocumentVector
from ..types import Vector
from .base import BaseDocumentVectorizerCore


class AllMiniLmVectorizerCore(BaseDocumentVectorizerCore):
    def __init__(self, model: SentenceTransformer):
        super(AllMiniLmVectorizerCore, self).__init__()
        self._model = model

    def vectorize(self, doc: Document) -> DocumentVector:
        return DocumentVector(vector=Vector.from_array(self._model.encode([doc.content])[0]))

    @classmethod
    def create(cls) -> "AllMiniLmVectorizerCore":
        return cls(SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2"))

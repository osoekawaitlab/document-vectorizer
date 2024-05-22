from sentence_transformers import SentenceTransformer

from ..models import Document, DocumentVector
from ..types import Vector
from .base import BaseDocumentVectorizerCore


class NomicEmbedTextCore(BaseDocumentVectorizerCore):
    def __init__(self, model: SentenceTransformer):
        super(NomicEmbedTextCore, self).__init__()
        self._model = model

    def vectorize(self, doc: Document) -> DocumentVector:
        return DocumentVector(vector=Vector.from_array(self._model.encode([doc.content])[0]))

    @classmethod
    def create(cls) -> "NomicEmbedTextCore":
        return cls(SentenceTransformer("nomic-ai/nomic-embed-text-v1.5", trust_remote_code=True))

__version__ = "0.0.1"

from .core import DocumentVectorizerCore
from .document_vectorizers.all_minilm import AllMiniLmVectorizer
from .document_vectorizers.nomic_embed_text import NomicEmbedTextVectorizer
from .models import Document, DocumentVector
from .types import DocumentContent, Scalar, Vector

__all__ = [
    "DocumentVectorizerCore",
    "Vector",
    "DocumentContent",
    "Scalar",
    "Document",
    "DocumentVector",
    "AllMiniLmVectorizer",
    "NomicEmbedTextVectorizer",
]

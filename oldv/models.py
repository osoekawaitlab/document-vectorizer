from oltl import BaseModel

from .types import DocumentContent, Vector


class DocumentVector(BaseModel):
    vector: Vector


class Document(BaseModel):
    content: DocumentContent

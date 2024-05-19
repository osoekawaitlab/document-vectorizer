from oltl import BaseModel as OltlBaseModel

from .types import DocumentContent, Vector


class BaseModel(OltlBaseModel):
    pass


class DocumentVector(BaseModel):
    vector: Vector


class Document(BaseModel):
    content: DocumentContent

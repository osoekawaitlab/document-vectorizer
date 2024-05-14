from oltl import BaseModel

from .types import Vector


class DocumentVector(BaseModel):
    vector: Vector

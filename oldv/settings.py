from enum import Enum
from typing import Annotated, Literal

from oltl.settings import BaseSettings
from pydantic import Field


class DocumentVectorizerType(str, Enum):
    COUNT = "COUNT"


class BaseDocumentVectorizerSettings(BaseSettings):
    type: DocumentVectorizerType


class CountVectorizerSettings(BaseDocumentVectorizerSettings):
    class Analyzer(str, Enum):
        WORD = "WORD"
        CHAR = "CHAR"

    type: Literal[DocumentVectorizerType.COUNT] = DocumentVectorizerType.COUNT
    analyzer: Analyzer = Field(default=Analyzer.WORD)


DocumentVectorizerSettings = Annotated[CountVectorizerSettings, Field(discriminator="type")]

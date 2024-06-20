from enum import Enum
from typing import Annotated, Literal, Union

from oltl.settings import BaseSettings as OltlBaseSettings
from pydantic import Field
from pydantic_settings import SettingsConfigDict


class BaseSettings(OltlBaseSettings):
    model_config = SettingsConfigDict(env_prefix="OLDV_")


class DocumentVectorizerType(str, Enum):
    ALL_MINI_LM = "ALL_MINI_LM"
    NOMIC_EMBED_TEXT = "NOMIC_EMBED_TEXT"


class BaseDocumentVectorizerSettings(BaseSettings):
    type: DocumentVectorizerType


class AllMiniLmDocumentVectorizerSettings(BaseDocumentVectorizerSettings):
    type: Literal[DocumentVectorizerType.ALL_MINI_LM] = DocumentVectorizerType.ALL_MINI_LM


class NomicEmbedTextDocumentVectorizerSettings(BaseDocumentVectorizerSettings):
    type: Literal[DocumentVectorizerType.NOMIC_EMBED_TEXT] = DocumentVectorizerType.NOMIC_EMBED_TEXT


DocumentVectorizerSettings = Annotated[
    Union[AllMiniLmDocumentVectorizerSettings, NomicEmbedTextDocumentVectorizerSettings],
    Field(discriminator="type"),
]


class DocumentVectorizerCoreSettings(BaseSettings):
    document_vectorizer_settings: DocumentVectorizerSettings

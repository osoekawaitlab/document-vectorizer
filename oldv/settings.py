from enum import Enum
from typing import Annotated, Literal, Union

from oltl.settings import BaseSettings as OltlBaseSettings
from pydantic import Field
from pydantic_settings import SettingsConfigDict


class BaseSettings(OltlBaseSettings):
    model_config = SettingsConfigDict(env_prefix="OLDV_")


class DocumentVectorizerModelType(str, Enum):
    ALL_MINI_LM = "ALL_MINI_LM"
    NOMIC_EMBED_TEXT = "NOMIC_EMBED_TEXT"


class BaseDocumentVectorizerSettings(BaseSettings):
    type: DocumentVectorizerModelType


class AllMiniLmDocumentVectorizerSettings(BaseDocumentVectorizerSettings):
    type: Literal[DocumentVectorizerModelType.ALL_MINI_LM] = DocumentVectorizerModelType.ALL_MINI_LM


class NomicEmbedTextDocumentVectorizerSettings(BaseDocumentVectorizerSettings):
    type: Literal[DocumentVectorizerModelType.NOMIC_EMBED_TEXT] = DocumentVectorizerModelType.NOMIC_EMBED_TEXT


DocumentVectorizerSettings = Annotated[
    Union[AllMiniLmDocumentVectorizerSettings, NomicEmbedTextDocumentVectorizerSettings],
    Field(discriminator="type"),
]


class DocumentVectorizerCoreSettings(BaseSettings):
    document_vectorizer_settings: DocumentVectorizerSettings


class DocumentVectorizerAppSettings(BaseSettings):
    core: DocumentVectorizerCoreSettings

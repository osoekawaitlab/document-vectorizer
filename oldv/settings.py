from enum import Enum
from typing import Annotated, Literal, Union

from oltl.settings import BaseSettings as OltlBaseSettings
from pydantic import Field
from pydantic_settings import SettingsConfigDict


class BaseSettings(OltlBaseSettings):
    model_config = SettingsConfigDict(env_prefix="OLDV_")


class DocumentVectorizerCoreType(str, Enum):
    ALL_MINI_LM = "ALL_MINI_LM"
    NOMIC_EMBED_TEXT = "NOMIC_EMBED_TEXT"


class BaseDocumentVectorizerCoreSettings(BaseSettings):
    type: DocumentVectorizerCoreType


class AllMiniLmVectorizerCoreSettings(BaseDocumentVectorizerCoreSettings):
    type: Literal[DocumentVectorizerCoreType.ALL_MINI_LM] = DocumentVectorizerCoreType.ALL_MINI_LM


class NomicEmbedTextVectorizerCoreSettings(BaseDocumentVectorizerCoreSettings):
    type: Literal[DocumentVectorizerCoreType.NOMIC_EMBED_TEXT] = DocumentVectorizerCoreType.NOMIC_EMBED_TEXT


DocumentVectorizerSettings = Annotated[
    Union[AllMiniLmVectorizerCoreSettings, NomicEmbedTextVectorizerCoreSettings],
    Field(discriminator="type"),
]


class DocumentVectorizerAppSettings(BaseSettings):
    document_vectorizer: DocumentVectorizerSettings

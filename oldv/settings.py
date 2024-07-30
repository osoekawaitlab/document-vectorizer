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


class BaseDocumentVectorizerModelSettings(BaseSettings):
    type: DocumentVectorizerModelType


class AllMiniLmDocumentVectorizerModelSettings(BaseDocumentVectorizerModelSettings):
    type: Literal[DocumentVectorizerModelType.ALL_MINI_LM] = DocumentVectorizerModelType.ALL_MINI_LM


class NomicEmbedTextDocumentVectorizerModelSettings(BaseDocumentVectorizerModelSettings):
    type: Literal[DocumentVectorizerModelType.NOMIC_EMBED_TEXT] = DocumentVectorizerModelType.NOMIC_EMBED_TEXT


DocumentVectorizerModelSettings = Annotated[
    Union[AllMiniLmDocumentVectorizerModelSettings, NomicEmbedTextDocumentVectorizerModelSettings],
    Field(discriminator="type"),
]


class DocumentVectorizerCoreSettings(BaseSettings):
    document_vectorizer_settings: DocumentVectorizerModelSettings


class InterfaceType(str, Enum):
    WEB_API = "WEB_API"
    CLI = "CLI"


class BaseInterfaceSettings(BaseSettings):
    type: InterfaceType


class WebApiInterfaceSettings(BaseInterfaceSettings):
    type: Literal[InterfaceType.WEB_API] = InterfaceType.WEB_API
    port: int
    host: str


class CliInterfaceSettings(BaseInterfaceSettings):
    type: Literal[InterfaceType.CLI] = InterfaceType.CLI


class DocumentVectorizerAppSettings(BaseSettings):
    core: DocumentVectorizerCoreSettings

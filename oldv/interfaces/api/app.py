from fastapi import FastAPI

from ...app import DocumentVectorizerApp
from ...models import Document, DocumentVector
from ...settings import DocumentVectorizerAppSettings


def gen_api_app() -> FastAPI:
    settings = DocumentVectorizerAppSettings()

    core_app = DocumentVectorizerApp.create(settings=settings)

    app = FastAPI()

    @app.get("/api/v1/vectorize", response_model=DocumentVector)
    def vectorize(text: str) -> DocumentVector:
        return core_app.vectorize(doc=Document(content=text))

    return app

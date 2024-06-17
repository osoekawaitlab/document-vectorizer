from fastapi import FastAPI

from ...app import DocumentVectorizerApp
from ...models import Document, Documents, DocumentVector, DocumentVectors
from ...settings import DocumentVectorizerAppSettings


def gen_api_app() -> FastAPI:
    settings = DocumentVectorizerAppSettings()

    core = DocumentVectorizerApp.create(settings=settings)

    app = FastAPI()

    @app.get("/api/v1/vectorize", response_model=DocumentVector)
    def vectorize(text: str) -> DocumentVector:
        return core.vectorize(doc=Document(content=text))

    @app.post("/api/v1/batch-vectorize", response_model=DocumentVectors)
    def batch_vectorize(documents: Documents) -> DocumentVectors:
        return DocumentVectors(document_vectors=core.batch_vectorize(docs=documents.documents))

    return app

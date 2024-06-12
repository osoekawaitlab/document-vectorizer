from fastapi import FastAPI

from ...app import DocumentVectorizerApp
from ...models import Document, Documents, DocumentVector, DocumentVectors
from ...settings import DocumentVectorizerAppSettings


def gen_api_app() -> FastAPI:
    settings = DocumentVectorizerAppSettings()

    core_app = DocumentVectorizerApp.create(settings=settings)

    app = FastAPI()

    @app.get("/api/v1/vectorize", response_model=DocumentVector)
    def vectorize(text: str) -> DocumentVector:
        return core_app.vectorize(doc=Document(content=text))

    @app.post("/api/v1/batch-vectorize", response_model=DocumentVectors)
    def batch_vectorize(documents: Documents) -> DocumentVectors:
        return DocumentVectors(document_vectors=core_app.batch_vectorize(docs=documents.documents))

    return app

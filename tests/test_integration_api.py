from fastapi.testclient import TestClient

from .document_vectorizers.fixtures import all_minilm_hello_world_vector


def test_api_accepts_single_document_json_output(api_app_client: TestClient) -> None:
    response = api_app_client.get(
        "/api/v1/vectorize",
        params={"text": "Hello world"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "vector" in data
    assert data["vector"] == all_minilm_hello_world_vector.tolist()

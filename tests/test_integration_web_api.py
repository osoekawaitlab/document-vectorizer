from fastapi.testclient import TestClient

from .document_vectorizers.fixtures import (
    all_minilm_hello_computer_vector,
    all_minilm_hello_world_vector,
)


def test_api_accepts_single_document_json_output(api_app_client: TestClient) -> None:
    response = api_app_client.get(
        "/api/v1/vectorize",
        params={"text": "Hello world"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "vector" in data
    assert data["vector"] == all_minilm_hello_world_vector.tolist()


def test_api_accepts_multiple_documents_jsonl_output(api_app_client: TestClient) -> None:
    response = api_app_client.post(
        "/api/v1/batch-vectorize",
        json={"documents": [{"content": "Hello world"}, {"content": "Hello computer"}]},
    )
    assert response.status_code == 200
    data_obj = response.json()
    assert "documentVectors" in data_obj
    data = data_obj["documentVectors"]
    assert len(data) == 2
    assert "vector" in data[0]
    assert data[0]["vector"] == all_minilm_hello_world_vector.tolist()
    assert "vector" in data[1]
    assert data[1]["vector"] == all_minilm_hello_computer_vector.tolist()

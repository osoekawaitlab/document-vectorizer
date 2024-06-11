import json
import os
import subprocess
import tempfile

from .document_vectorizers.fixtures import (
    all_minilm_hello_computer_vector,
    all_minilm_hello_world_vector,
)


def test_cli_run_single_document_json_file_output(patch_all_minilm_environment_variable: None) -> None:
    with tempfile.TemporaryDirectory() as tempdir:
        output_file_name = "output.json"
        error_code = subprocess.run(
            [
                "oldv",
                "vectorize",
                "Hello World",
                os.path.join(tempdir, output_file_name),
            ],
            env=os.environ,
        )
        assert error_code.returncode == 0
        with open(os.path.join(tempdir, output_file_name), "r") as output_file:
            data = json.load(output_file)
        assert "vector" in data
        assert data["vector"] == all_minilm_hello_world_vector.tolist()


def test_cli_run_multiple_document_jsonl_file_output(patch_all_minilm_environment_variable: None) -> None:
    with tempfile.TemporaryDirectory() as tempdir:
        input_file_name = "input.jsonl"
        with open(os.path.join(tempdir, input_file_name), "w") as input_file:
            json.dump({"content": "Hello World"}, input_file)
            input_file.write("\n")
            json.dump({"content": "Hello Computer"}, input_file)
            input_file.write("\n")
        output_file_name = "output.jsonl"
        error_code = subprocess.run(
            [
                "oldv",
                "batch-vectorize",
                os.path.join(tempdir, input_file_name),
                os.path.join(tempdir, output_file_name),
            ],
            stdout=subprocess.PIPE,
            env=os.environ,
        )
        assert error_code.returncode == 0
        with open(os.path.join(tempdir, output_file_name), "r") as output_file:
            data = [json.loads(line) for line in output_file]
        assert len(data) == 2
        assert "vector" in data[0]
        assert data[0]["vector"] == all_minilm_hello_world_vector.tolist()
        assert "vector" in data[1]
        assert data[1]["vector"] == all_minilm_hello_computer_vector.tolist()

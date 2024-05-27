import json
import os
import subprocess
import tempfile

from .document_vectorizers.fixtures import all_minilm_hello_world_vector


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

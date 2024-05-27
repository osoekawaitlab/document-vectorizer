import json
import os
import subprocess
import tempfile


def test_cli_run_single_document_json_file_output() -> None:
    with tempfile.TemporaryDirectory() as tempdir:
        output_file_name = "output.json"
        subprocess.run(
            [
                "oldv",
                "vectorize",
                "Hello World",
                os.path.join(tempdir, output_file_name),
            ],
            check=True,
        )
        with open(os.path.join(tempdir, output_file_name), "r") as output_file:
            data = json.load(output_file)
        assert "vector" in data
        for v in data["vector"]:
            assert isinstance(v, float)

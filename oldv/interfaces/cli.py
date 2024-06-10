from argparse import ArgumentParser

from ..app import DocumentVectorizerApp
from ..models import Document
from ..settings import DocumentVectorizerAppSettings


def main() -> None:
    parser = ArgumentParser()
    subcommand_parser = parser.add_subparsers(dest="subcommand")
    vectorize_parser = subcommand_parser.add_parser("vectorize")
    vectorize_parser.add_argument("text")
    vectorize_parser.add_argument("output_file")
    args = parser.parse_args()
    if args.subcommand == "vectorize":
        settings = DocumentVectorizerAppSettings()
        app = DocumentVectorizerApp.create(settings=settings)
        document_vector = app.vectorize(doc=Document(content=args.text))
        output_file = args.output_file
        with open(output_file, "w") as f:
            f.write(document_vector.model_dump_json())

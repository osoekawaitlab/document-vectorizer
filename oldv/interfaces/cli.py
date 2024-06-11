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
    batch_vectorize_parser = subcommand_parser.add_parser("batch-vectorize")
    batch_vectorize_parser.add_argument("input_file")
    batch_vectorize_parser.add_argument("output_file")
    args = parser.parse_args()
    if args.subcommand == "vectorize":
        settings = DocumentVectorizerAppSettings()
        app = DocumentVectorizerApp.create(settings=settings)
        document_vector = app.vectorize(doc=Document(content=args.text))
        output_file = args.output_file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(document_vector.model_dump_json())
    elif args.subcommand == "batch-vectorize":
        settings = DocumentVectorizerAppSettings()
        app = DocumentVectorizerApp.create(settings=settings)
        with open(args.input_file, "r", encoding="utf-8") as f:
            documents = [Document.model_validate_json(line) for line in f]
        document_vectors = app.batch_vectorize(docs=documents)
        output_file = args.output_file
        with open(output_file, "w", encoding="utf-8") as f:
            for document_vector in document_vectors:
                f.write(document_vector.model_dump_json())
                f.write("\n")

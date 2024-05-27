from argparse import ArgumentParser


def main() -> None:
    parser = ArgumentParser()
    subcommand_parser = parser.add_subparsers(dest="subcommand")
    vectorize_parser = subcommand_parser.add_parser("vectorize")
    vectorize_parser.add_argument("text")
    vectorize_parser.add_argument("output_file")
    args = parser.parse_args()
    if args.subcommand == "vectorize":
        text = args.text
        output_file = args.output_file
        with open(output_file, "w") as f:
            f.write(f'{{"vector": [{", ".join(str(v) for v in [1.0, 2.0, 3.0])}]}}\n')

"""Python Swagger Codegen

This script allows to generate Python code from swagger openapi spec.
"""

import argparse
import subprocess
from typing import Tuple

DEFAULT_PATH = "output"
DEFAULT_SOURCE = (
    "https://test.openbankproject.com/obp/v5.0.0/resource-docs/v5.0.0/swagger"
)


def parse_arguments() -> Tuple[str, str]:
    """Read command line argument options."""
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "--output",
        help="where to write the generated files (output dir by default).",
        type=str,
        default=DEFAULT_PATH,
    )
    argument_parser.add_argument(
        "--source",
        help="location of the swagger spec, as URL or file (required).",
        type=str,
        default=DEFAULT_SOURCE,
    )
    args = argument_parser.parse_args()
    output = args.output
    source = args.source
    return (output, source)


def generate() -> None:
    """Generate Python code out of open api spec using swaggger-codegen-cli."""

    [output, source] = parse_arguments()

    subprocess.call(
        [
            "java",
            "-jar",
            "swagger-codegen-cli-2.2.1.jar",
            "generate",
            "-i",
            f"{source}",
            "-l",
            "python",
            "-o",
            f"{output}",
            "-c",
            "config.json",
        ]
    )


if __name__ == "__main__":
    generate()

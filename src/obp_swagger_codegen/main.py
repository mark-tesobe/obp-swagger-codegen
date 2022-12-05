"""Python Swagger Codegen

This script allows to generate Python code from swagger openapi spec.
"""

import argparse
import subprocess
from typing import List, Tuple

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


def remove_line_file(lines_to_remove: List[str], file_path: str) -> None:
    """Remove a line in a specified file."""

    with open(file_path, "+r") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if line.rstrip() not in lines_to_remove:
                file.write(line)
                file.truncate()
            else:
                print(f"Removing line `{line}` from {file_path}")


def clean_imports() -> None:
    """Remove invalid module import."""

    print("Cleaning imports..")
    imports_to_remove = [
        "from obp_python.models.consumer_json import ConsumerJSON",
        "from obp_python.models.metrics_json import MetricsJSON",
    ]
    file_name = "__init__.py"
    files = [
        f"{DEFAULT_PATH}/obp_python/{file_name}",
        f"{DEFAULT_PATH}/obp_python/models/{file_name}",
    ]
    for file in files:
        remove_line_file(imports_to_remove, file)
    # for file in files:
    #    for line_to_remove in imports_to_remove:
    #        remove_line_file(line_to_remove, file)
    print("Done cleaning imports.")


def generate() -> None:
    """Generate Python code out of open api spec using swaggger-codegen-cli."""

    [output, source] = parse_arguments()

    subprocess.call(
        [
            "java",
            "-jar",
            "swagger-codegen-cli-2.4.29.jar",
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

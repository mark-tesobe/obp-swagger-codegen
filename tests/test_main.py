import os

import obp_swagger_codegen.main as obp_sc


def test_parse_arguments() -> None:
    [path, source] = obp_sc.parse_arguments()
    assert path == obp_sc.DEFAULT_PATH
    assert source == obp_sc.DEFAULT_SOURCE


def test_remove_line_file() -> None:
    content = "line1\nline2\nline3"
    path = "tmp.txt"

    # create tmp file
    with open(path, "w") as file:
        file.write(content)

    obp_sc.remove_line_file(["line3"], path)

    with open(path, "+r") as file:
        lines = file.readlines()
        assert "line3" not in lines

    # remove tmp test file
    os.remove(path)

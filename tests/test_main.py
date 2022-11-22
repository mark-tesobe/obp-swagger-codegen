import src.obp_swagger_codegen.main as obp_sc


def test_pars_arguments() -> None:
    [path, source] = obp_sc.parse_arguments()
    assert path == obp_sc.DEFAULT_PATH
    assert source == obp_sc.DEFAULT_SOURCE

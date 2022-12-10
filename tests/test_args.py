from tools.utils.args_parse import parse_arguments
from tools.utils.logger import logger

import pytest


def test_default_parse_arguments():
    run_opts = parse_arguments()
    assert run_opts["debug"] == False


def test_set_parse_arguments():
    args_list = ["--debug"]
    run_opts = parse_arguments(args_list)
    assert run_opts["debug"] == True

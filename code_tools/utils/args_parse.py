import argparse
import sys
# help flag provides flag help


def parse_arguments(arg_list=None):
    if arg_list is None:
        arg_list = sys.argv[1:]
    parser = argparse.ArgumentParser(description="Run a task of cronjob")
    parser.add_argument(
        "--debug",
        default=False,
        action="store_true",
        help="Run the task with little dataset and log_level=debug",
    )

    # Accept extra args to override yaml
    run_opts = parser.parse_args(arg_list)

    # Ignore items that are "None", they were not passed
    run_opts = {k: v for k, v in vars(run_opts).items() if v is not None}

    # param_file = run_opts["param_file"]
    # del run_opts["param_file"]
    return run_opts
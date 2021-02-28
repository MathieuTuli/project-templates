"""
@author: Mathieu Tuli
@github: MathieuTuli
@email: tuli.mathie@gmail.com
"""
from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path

from .utils.logging import LogLevel, init_logger
from .args import logging_args

parser = ArgumentParser(description="TOD")
parser.add_argument(
    '--logs', help="Set output for log outputs",
    default=f"logs/tod_{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.log",)
subparser = parser.add_subparsers(dest='command')
logging_args(parser)
example = subparser.add_parser(
    'example', help="run 'python -m tod example --help' for example arguments",
    parents=[parser], add_help=False)
# example_args(example)

args = parser.parse_args()
if args.verbose:
    args.log_level = LogLevel.DEBUG
logger = init_logger(Path(args.logs),
                     log_level=args.log_level)
nf str(args.command) == 'example':
    ...
else:
    logger.critical(f"Unknown subcommand {args.command}")

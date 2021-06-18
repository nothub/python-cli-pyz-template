import argparse
from pathlib import Path


def non_empty_string(s):
    s = str(s)
    if not s or not s.isprintable():
        raise argparse.ArgumentTypeError("invalid argument! string is empty")
    return s


def positive_int(n: str) -> int:
    n = int(n)
    if n < 1:
        raise argparse.ArgumentTypeError("invalid argument! out of range")
    return n


def network_port(n: str) -> int:
    n = int(n)
    if n < 1 or n > 65535:
        raise argparse.ArgumentTypeError("invalid argument! out of range")
    return n


def file_path(s: str):
    path = Path(s)
    if path is None or (path.exists() and not path.is_file()):
        raise argparse.ArgumentTypeError("invalid argument! not a valid file path")
    return path


def dir_path(s: str):
    path = Path(s)
    if path is None or (path.exists() and not path.is_dir()):
        raise argparse.ArgumentTypeError("invalid argument! not a valid directoy path")
    return path

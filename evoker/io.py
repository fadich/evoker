import sys


def writeln(line: str):
    sys.stdout.write(f"{line}\n")
    sys.stdout.flush()


def writeln_err(line: str):
    sys.stderr.write(f"{line}\n")
    sys.stderr.flush()

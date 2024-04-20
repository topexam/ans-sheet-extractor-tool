import argparse
import sys
from pathlib import Path

from src.entry import entry_point
from src.logger import logger


if __name__ == "__main__":
    sys.tracebacklimit = 0
    entry_point(Path("inputs"))

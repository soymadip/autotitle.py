"""
Core functionality for the autotitle package.
"""

from typing import Optional

from logger import logger
from utils import default_path


def rename(
    input_dir: str = ".", series: str = "dc", custom_db_dir: Optional[str] = None
):
    """
    Main renamer function for the autotitle package.
    fetch fillers, names, reange files, and rename episodes.

    Args:
        input_dir (str): Directory containing episodes to rename
        series (str): Series name matching a folder in the db directory
        custom_db_dir (str, optional): Custom database directory path
    """

    logger.warning("Yet to be done")

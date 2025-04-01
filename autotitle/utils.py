from logger import Logger
from types import Optional


def default_path(file_name: str = "db"):
    Logger.warning(f"Default path is {file_name}")

    
def list_series(path: Optional(str) = default_path()):
    """
    List all series in the database.

    Args:
        path (str): Path to the database. (defaults to package database)

    Returns:
        list: A list of series names.

    Example:
        >>> list_series()
        ['series1', 'series2', 'series3']
    """
    pass
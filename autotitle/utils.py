from logger import Logger


def default_path(file_name: str = "db") -> None:
    Logger.warning(f"Default path is {file_name}")

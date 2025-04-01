"""
Logger module for autotitle package.
Provides colored console output for various types of messages.
"""


# ANSI color codes for colored terminal output
class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    DIM = "\033[2m"
    ENDC = "\033[0m"


class logger:
    """logger for for autotitle"""

    @staticmethod
    def info(message):
        """Log informational message in cyan"""
        print(f"{Colors.CYAN}{message}{Colors.ENDC}")

    @staticmethod
    def success(message):
        """Log success message in green"""
        print(f"{Colors.GREEN}{message}{Colors.ENDC}")

    @staticmethod
    def warning(message):
        """Log warning message in yellow"""
        print(f"{Colors.YELLOW}{message}{Colors.ENDC}")

    @staticmethod
    def error(message):
        """Log error message in red"""
        print(f"{Colors.RED}{message}{Colors.ENDC}")

    @staticmethod
    def header(message):
        """Log header message in bold purple"""
        print(f"\n{Colors.BOLD}{Colors.HEADER}{message}{Colors.ENDC}\n")

    @staticmethod
    def summary(title, content):
        """Log summary with title in bold purple and content in default color"""
        print(f"\n{Colors.BOLD}{Colors.HEADER}{title}:{Colors.ENDC} {content}")

    @staticmethod
    def renamed(old_filename, new_filename, is_movie=False, series=None):
        """Log file rename operation with old name dimmed and new name in green/blue"""
        color = Colors.BLUE if is_movie else Colors.GREEN
        series_info = f" [{series}]" if series else ""
        print(f"{Colors.DIM}=> {old_filename}{Colors.ENDC}")
        print(f"{color}   └─> {new_filename}{Colors.DIM}{series_info}{Colors.ENDC}\n")

    @staticmethod
    def series_info(series, count):
        """Log series information"""
        print(
            f"{Colors.CYAN}Series: {Colors.BOLD}{series}{Colors.ENDC} - {count} files found"
        )

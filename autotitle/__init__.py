"""
Autotitle - Episode renamer with proper titles.
"""

import importlib.metadata

from typing import Tuple, Optional
from .main import rename

# Get the version of the package
try:
    __version__ = importlib.metadata.version("autotitle")

except importlib.metadata.PackageNotFoundError:
    __version__ = "N/A"

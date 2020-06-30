import os
from pathlib import Path


def get_project_root() -> Path:
    """Returns project root folder."""
    return Path(__file__).parent.parent


PROJECT_ROOT = get_project_root()

DATA_ROOT = os.path.join(project_root, 'data')


__all__ = [
    'DATA_ROOT',
    'PROJECT_ROOT'
]

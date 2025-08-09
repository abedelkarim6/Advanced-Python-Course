print("Hello from feature1.py!")

from utils import utils  # ✅ absolute import, works when running as a module

# from . import main            # ❌ relative import, will raise ImportError if run as a script
# from ..utils import utils     # ❌ relative import, will raise ImportError if run as a script

# from .. import test  # ❌ relative import, will raise ImportError

# -------------------PLAN B-------------------
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import utils
import test


# Explanation:
# Add the parent directory of this file to the Python path.
# This allows us to import modules from sibling directories (e.g., utils/) when running this file directly (e.g., `python feature1.py`).
# Without this, Python only searches for modules in the current directory and sys.path, and may raise ImportError.
# This is a common workaround when not using the project as a package (i.e., not running via `python -m` or installing it).

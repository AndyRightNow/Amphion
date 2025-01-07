from pathlib import Path
import os

maskgct_config_file = Path(os.path.dirname(
    os.path.realpath(__file__)), 'config/maskgct.json').resolve()

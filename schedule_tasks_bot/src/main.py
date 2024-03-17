import os
import sys

app_dir = os.path.abspath(os.path.dirname(__file__))
if app_dir not in sys.path:
  sys.path.append(app_dir)

from bootstraps import Bootstrap, app
from core.helpers.load_module import load_module

load_module('*/schedulers/*.py')

Bootstrap(app)

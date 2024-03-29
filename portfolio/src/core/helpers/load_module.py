import glob
import importlib


def load_module(path: str):
  modules = glob.glob(path, recursive=True)
  for module in modules:
    importlib.import_module(
      module.replace('.py', '').replace('/', '.').replace('portfolio.src.', ''),
      package=None,
    )

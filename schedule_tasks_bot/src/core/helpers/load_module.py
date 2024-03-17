import glob
import importlib
import threading


def load_module(path: str):
  modules = glob.glob(path, recursive=True)
  for module in modules:
    importlib.import_module(
      module.replace('.py', '').replace('/', '.').replace('schedule_tasks_bot.src.', ''),
      package=None,
    )


def start_load_module_thread(threads, path):
  thread = threading.Thread(target=load_module, args=(path,))
  thread.start()
  threads.append(thread)


def load_modules(paths: list[str]):
  threads = []

  for path in paths:
    start_load_module_thread(threads, path)

  for thread in threads:
    thread.join()

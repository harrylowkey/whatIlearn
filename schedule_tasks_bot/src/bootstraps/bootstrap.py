from fastapi import FastAPI
from starlette.staticfiles import StaticFiles


class Bootstrap:
  def __init__(self, app: FastAPI):
    self.app = app
    self.mount_static_folder()

  def mount_static_folder(self):
    self.app.mount('/static', StaticFiles(directory='schedule_tasks_bot/src/static'), name='static')

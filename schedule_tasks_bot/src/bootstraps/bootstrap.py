from fastapi import FastAPI


class Bootstrap:
  def __init__(self, app: FastAPI):
    self.app = app

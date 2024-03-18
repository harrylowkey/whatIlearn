import os

from dotenv import dotenv_values

loaded_env = dotenv_values('schedule_tasks_bot/.env')


def get_env(key, default=None):
  if key in loaded_env:
    return loaded_env.get(key)
  if os.getenv(key):
    return os.getenv(key)
  return default


class Setting:
  SLACK_TOKEN = get_env('SLACK_TOKEN')
  IS_LOCAL = get_env('ENV', 'local') == 'local'
  WEB_URL = 'http://localhost:3000' if IS_LOCAL else 'http://harrylowkey.online'


env = Setting()

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from config import env


class Slack:
  SCHEDULE_TAKS_CHANNEL_ID = '#schedule-tasks'

  def __init__(self):
    self.client = WebClient(token=env.SLACK_TOKEN)

  def send_tasks_to_slack(self, tasks, message_prefix):
    if not tasks:
      return

    try:
      tasks_text = '\n'.join(tasks)
      message = f'*{message_prefix}*\n\n{tasks_text}'
      self.client.chat_postMessage(channel=self.SCHEDULE_TAKS_CHANNEL_ID, text=message)
    except SlackApiError as e:
      print(f"Error sending message to Slack: {e.response['error']}")


SlackBot = Slack()

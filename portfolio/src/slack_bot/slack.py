from config import env
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class Slack:
  SCHEDULE_TAKS_CHANNEL_ID = '#schedule-tasks'

  def __init__(self):
    self.client = WebClient(token=env.SLACK_TOKEN)

  def send_tasks_to_slack(self, tasks, message_prefix):
    if not tasks:
      tasks = self.generate_default_task()

    tasks_text = self.format_tasks(tasks)
    message = self.compose_message(message_prefix, tasks_text)

    try:
      self.send_message_to_slack(message)
    except SlackApiError as e:
      print(f"Error sending message to Slack: {e.response['error']}")

  def generate_default_task(self):
    return [
      {
        'status': '❌',
        'task_type': '',
        'annotation': '',
        'description': "- 🙉 There are no tasks anymore. Let's fucking hustle or you'll be broken 🔥!",
      }
    ]

  def format_tasks(self, tasks):
    tasks_text = []
    for task in tasks:
      status, task_type, annotation, description = task.values()
      task_text = f'{status} [{task_type}] {annotation} {description}'
      tasks_text.append(task_text)

    return '\n'.join(tasks_text)

  def compose_message(self, message_prefix, tasks_text):
    return f'*{message_prefix}*\n\n{tasks_text}'

  def send_message_to_slack(self, message):
    self.client.chat_postMessage(channel=self.SCHEDULE_TAKS_CHANNEL_ID, text=message)

SlackBot = Slack()

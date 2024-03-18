from config import env
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class Slack:
  SCHEDULE_TAKS_CHANNEL_ID = '#schedule-tasks'

  def __init__(self):
    self.client = WebClient(token=env.SLACK_TOKEN)

  def send_tasks_to_slack(self, tasks, message_prefix):
    if not tasks:
      tasks = [
        {
          'status': '❌',
          'task_type': '',
          'annotation': '',
          'description': "- 🙉 There are no tasks anymore. Let's fucking hustle or you'll be broken 🔥!",
        }
      ]

    tasks_text = []
    for task in tasks:
      status, task_type, annotation, description = task.values()
      task_text = f'{status} [{task_type}] {annotation} {description}'
      tasks_text.append(task_text)

    tasks_text = '\n'.join(tasks_text)
    message = f'*{message_prefix}*\n\n{tasks_text}'

    try:
      self.client.chat_postMessage(channel=self.SCHEDULE_TAKS_CHANNEL_ID, text=message)
    except SlackApiError as e:
      print(f"Error sending message to Slack: {e.response['error']}")


SlackBot = Slack()

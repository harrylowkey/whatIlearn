import re
from datetime import datetime, timedelta

from bs4 import BeautifulSoup
from markdown2 import markdown
from slack_bot.slack import SlackBot


def extract_tasks_from_list(ul_tag):
  tasks = []
  if ul_tag:
    task_items = ul_tag.find_all('li')
    for task_item in task_items:
      task_text = task_item.text.strip()
      pattern = re.compile(r'\[(x| )\]\s*\[(.*?)\]\s*(?:\((.*?)\))?\s*(.*)')
      match = pattern.match(task_text)

      if match:
        status = match.group(1)
        task_type = match.group(2)
        annotation = match.group(3)
        description = match.group(4)

        status = '- ✅' if status == 'x' else '- ⌛'
        annotation = f'({annotation})' if annotation else ''

        tasks.append(f'{status} [{task_type}] {annotation} {description}')

  return tasks


def get_backlog_tasks(markdown_content):
  tasks = {}

  task_sections = [
    ('Ongoing tasks:', 'Ongoing tasks'),
    ('High priority tasks:', 'High priority tasks'),
    # ("Medium priority tasks:", "Medium priority tasks"),
    # ("Low priority tasks:", "Low priority tasks"),
  ]

  soup = BeautifulSoup(markdown(markdown_content), 'html.parser')

  for section_title, task_key in task_sections:
    section = soup.find('h3', string=section_title)
    if section:
      tasks[task_key] = extract_tasks_from_list(section.find_next_sibling('ul'))

  return tasks


def get_daily_tasks(markdown_content):
  today_date = datetime.now().strftime('%b-%d')
  tasks_by_date = {}

  soup = BeautifulSoup(markdown_content, 'html.parser')
  date_tags = soup.find_all('h4')

  for date_tag in date_tags:
    date = date_tag.text.strip()

    tasks = []
    task_list = date_tag.find_next('ul')
    task_items = task_list.find_all('li')

    for task_item in task_items:
      soup = BeautifulSoup(str(task_item), 'html.parser')
      task_item = soup.find('li').text

      pattern = re.compile(r'\[(x| )\]\s*\[(.*?)\]\s*(?:\((.*?)\))?\s*(.*)')
      match = pattern.match(task_item)

      if match:
        status = match.group(1)
        task_type = match.group(2)
        annotation = match.group(3)
        description = match.group(4)

        annotation = f'({annotation})' if annotation else ''
        if status == 'x':
          status = '- ✅' if date != today_date else '- ✅'
        else:
          status = '- ❌' if date != today_date else '- ⌛'

        tasks.append(f'{status} [{task_type}] {annotation} {description}')

    tasks_by_date[date] = tasks

  return tasks_by_date


def get_tasks(markdown_content):
  tasks_by_date = get_daily_tasks(markdown_content)
  backlog_tasks = get_backlog_tasks(markdown_content)
  return tasks_by_date, backlog_tasks


def send_daily_tasks(tasks_by_date):
  today_date = datetime.now().strftime('%b-%d')
  today_tasks = tasks_by_date.get(today_date, [])

  SlackBot.send_tasks_to_slack(today_tasks, f"Today's tasks ({today_date}):")

  yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%b-%d')
  yesterday_tasks = tasks_by_date.get(yesterday_date, [])
  SlackBot.send_tasks_to_slack(yesterday_tasks, f"Yesterday's tasks ({yesterday_date}):")


def send_backlog_tasks(backlog_tasks):
  for task_type, tasks in backlog_tasks:
    SlackBot.send_tasks_to_slack(tasks, f'{task_type}:')


def send_tasks():
  with open('schedule_tasks_bot/SCHEDULE.md', 'r', encoding='utf-8') as file:
    markdown_content = file.read()

  tasks_by_date, backlog_tasks = get_tasks(markdown(markdown_content))

  print('Start sending tasks')

  send_daily_tasks(tasks_by_date)
  send_backlog_tasks(backlog_tasks.items())

  print('Sent tasks successfully')

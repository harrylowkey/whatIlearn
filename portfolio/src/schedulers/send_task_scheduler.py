from bootstraps import app
from config import scheduler

from services.schedule_task import ScheduleTaskService


def send_tasks():
  tasks_by_date, backlog_tasks = ScheduleTaskService.get_tasks()

  print('Start sending tasks')
  ScheduleTaskService.send_daily_tasks(tasks_by_date)
  ScheduleTaskService.send_backlog_tasks(backlog_tasks.items())
  print('Sent tasks successfully')


@app.on_event('startup')
def send_tasks_scheduler():
  scheduler.add_job(send_tasks, 'cron', hour=1)

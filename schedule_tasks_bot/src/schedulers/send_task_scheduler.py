from bootstraps import app
from config import scheduler
from tasks.task import send_tasks


@app.on_event('startup')
def send_tasks_scheduler():
  scheduler.add_job(send_tasks, 'cron', hour=7)

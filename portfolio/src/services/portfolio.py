from datetime import datetime, timedelta

from fastapi import Request

from config import env
from portfolio.src.helpers.render_badge_classes import render_badge_classes
from portfolio.src.services.project import ProjectService
from services.note import NoteService
from services.schedule_task import ScheduleTaskService


class PortfolioService:
  @staticmethod
  def prepare_tasks(request: Request):
    tasks_by_date, backlog_tasks = ScheduleTaskService.get_tasks()

    today_date = datetime.now().strftime('%b-%d')
    today_tasks = tasks_by_date.get(today_date, [])

    yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%b-%d')
    yesterday_tasks = tasks_by_date.get(yesterday_date, [])

    high_priority_tasks = backlog_tasks['High priority tasks']

    return {
      'request': request,
      'WEB_URL': env.WEB_URL,
      'today_tasks': today_tasks,
      'total_today_tasks': len(today_tasks),
      'yesterday_tasks': yesterday_tasks,
      'total_yesterday_tasks': len(yesterday_tasks),
      'high_priority_tasks': high_priority_tasks,
      'total_high_priority_tasks': len(high_priority_tasks),
    }

  @staticmethod
  def prepare_notes(request: Request, page: int):
    notes, total_notes, prev_page, next_page = NoteService.paginate(page)

    return {
      'request': request,
      'total_notes': total_notes,
      'notes': notes,
      'current_page': page,
      'prev_page': prev_page,
      'next_page': next_page,
      'WEB_URL': env.WEB_URL,
      'render_badge_classes': render_badge_classes,
    }

  @staticmethod
  def prepare_note(request: Request, title: str):
    note = NoteService.fetch_notes(file_name=f'{title}.md')

    return {
      'request': request,
      'note': note,
    }

  @staticmethod
  def prepare_projects(request: Request):
    projects = ProjectService.fetch_projects()

    return {'request': request, 'projects': projects, 'total_projects': len(projects), 'WEB_URL': env.WEB_URL}

  @staticmethod
  def prepare_project(request: Request, name: str):
    project = ProjectService.fetch_projects(file_name=f'{name}.md')

    return {
      'request': request,
      'project': project,
    }

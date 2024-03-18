from datetime import datetime, timedelta

from bootstraps import app
from config import env
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from markdown2 import markdown
from models.note import fetch_notes
from schedule_tasks.src.helpers.render_badge_classes import render_badge_classes
from schedule_tasks.src.schedule_tasks.task import get_tasks

templates = Jinja2Templates(directory='schedule_tasks/src/templates')
POSTS_PER_PAGE = 6


@app.get('/', response_class=HTMLResponse)
async def index(request: Request, page: int = 1):
  with open('schedule_tasks/SCHEDULE.md', 'r', encoding='utf-8') as file:
    markdown_content = file.read()

  tasks_by_date, backlog_tasks = get_tasks(markdown(markdown_content))

  today_date = datetime.now().strftime('%b-%d')
  today_tasks = tasks_by_date.get(today_date, [])

  yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%b-%d')
  yesterday_tasks = tasks_by_date.get(yesterday_date, [])

  high_priority_tasks = backlog_tasks['High priority tasks']

  return templates.TemplateResponse(
    'pages/tasks/index.html',
    {
      'request': request,
      'WEB_URL': env.WEB_URL,
      'today_tasks': today_tasks,
      'total_today_tasks': len(today_tasks),
      'yesterday_tasks': yesterday_tasks,
      'total_yesterday_tasks': len(yesterday_tasks),
      'high_priority_tasks': high_priority_tasks,
      'total_high_priority_tasks': len(high_priority_tasks),
    },
  )


@app.get('/projects', response_class=HTMLResponse)
async def projects(request: Request):
  return templates.TemplateResponse('pages/projects/index.html', {'request': request, 'WEB_URL': env.WEB_URL})


@app.get('/notes', response_class=HTMLResponse)
async def notes(request: Request, page: int = 1):
  notes = fetch_notes()

  total_notes = len(notes)
  start_idx = (page - 1) * POSTS_PER_PAGE
  end_idx = start_idx + POSTS_PER_PAGE

  prev_page = page - 1 if page > 1 else None
  next_page = page + 1 if end_idx < total_notes else None

  notes = notes[start_idx:end_idx]

  return templates.TemplateResponse(
    'pages/notes/index.html',
    {
      'request': request,
      'total_notes': total_notes,
      'notes': notes,
      'current_page': page,
      'prev_page': prev_page,
      'next_page': next_page,
      'WEB_URL': env.WEB_URL,
      'render_badge_classes': render_badge_classes,
    },
  )


@app.get('/notes/{note_title}', response_class=HTMLResponse)
async def note(request: Request, note_title: str):
  note = fetch_notes(f'{note_title}.md')

  return templates.TemplateResponse(
    'pages/notes/note-detail.html',
    {
      'request': request,
      'note': note,
    },
  )

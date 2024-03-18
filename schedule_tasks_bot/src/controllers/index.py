from bootstraps import app
from config import env
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.note import fetch_notes

templates = Jinja2Templates(directory='schedule_tasks_bot/src/templates')
POSTS_PER_PAGE = 6


@app.get('/', response_class=HTMLResponse)
async def index(request: Request, page: int = 1):
  return templates.TemplateResponse('pages/tasks/index.html', {'request': request, 'WEB_URL': env.WEB_URL})


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

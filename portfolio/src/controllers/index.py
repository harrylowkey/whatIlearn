from fastapi import Request
from fastapi.responses import HTMLResponse

from bootstraps import app
from services.portfolio import PortfolioService
from services.template import TemplateService
from services.view_count import update_view_count


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
  update_view_count('index')
  return TemplateService.render('pages/tasks/index.html', PortfolioService.prepare_tasks(request))


@app.get('/projects', response_class=HTMLResponse)
async def projects(request: Request):
  update_view_count('projects')
  return TemplateService.render('pages/projects/index.html', PortfolioService.prepare_projects(request))


@app.get('/projects/{name}', response_class=HTMLResponse)
async def project(request: Request, name: str):
  update_view_count(f'projects/{name}')
  return TemplateService.render('pages/projects/project-detail.html', PortfolioService.prepare_project(request, name))


@app.get('/notes', response_class=HTMLResponse)
async def notes(request: Request, page: int = 1, key: str | None = None):
  update_view_count('notes')
  return TemplateService.render('pages/notes/index.html', PortfolioService.prepare_notes(request, page, key))


@app.get('/notes/{title}', response_class=HTMLResponse)
async def note(request: Request, title: str):
  update_view_count(f'notes/{title}')
  return TemplateService.render('pages/notes/note-detail.html', PortfolioService.prepare_note(request, title))

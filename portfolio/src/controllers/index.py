from bootstraps import app
from config import env
from fastapi import Request
from fastapi.responses import HTMLResponse

from portfolio.services.portfolio import PortfolioService
from portfolio.services.template import TemplateService


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
  return TemplateService.render('pages/tasks/index.html', PortfolioService.prepare_tasks(request))


@app.get('/projects', response_class=HTMLResponse)
async def projects(request: Request):
  return TemplateService.render('pages/projects/index.html', {'request': request, 'WEB_URL': env.WEB_URL})


@app.get('/notes', response_class=HTMLResponse)
async def notes(request: Request, page: int = 1):
  return TemplateService.render('pages/notes/index.html', PortfolioService.prepare_notes(request, page))


@app.get('/notes/{title}', response_class=HTMLResponse)
async def note(request: Request, title: str):
  return TemplateService.render('pages/notes/note-detail.html', PortfolioService.prepare_note(request, title))

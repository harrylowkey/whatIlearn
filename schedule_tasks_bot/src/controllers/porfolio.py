from bootstraps import app
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.article import fetch_articles

templates = Jinja2Templates(directory='schedule_tasks_bot/src/templates')


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
  return templates.TemplateResponse('index.html', {'request': request})

@app.get('/projects', response_class=HTMLResponse)
async def projects(request: Request):
    return templates.TemplateResponse('projects.html', {'request': request})


@app.get('/blogs', response_class=HTMLResponse)
async def blogs(request: Request):
  articles = fetch_articles()
  return templates.TemplateResponse('index.html', {'request': request, 'article': articles[0], 'articles': articles})

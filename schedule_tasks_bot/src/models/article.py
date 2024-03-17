import os

from markdown2 import markdown


class Article:
  def __init__(self, title, content):
    self.title = title
    self.content = content


def fetch_articles():
  articles = []
  for root, dirs, files in os.walk('notes'):
    for file in files:
      if file.endswith('.md'):
        with open(f'{root}/{file}', 'r') as f:
          markdown_content = f.read()
        html_content = markdown(markdown_content)
        article = Article(title=file.split('/')[-1].split('.')[0], content=html_content)
        articles.append(article)
  return articles

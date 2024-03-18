import os

from bs4 import BeautifulSoup, Comment
from markdown2 import markdown


class Note:
  def __init__(self, title, file_path, published_date, description, tags, content):
    self.title = title
    self.file_path = file_path
    self.description = description
    self.content = content
    self.tags = tags
    self.published_date = published_date


def read_markdown_file(file_path):
  with open(file_path, 'r') as f:
    markdown_content = f.read()
  return markdown_content


def parse_html_content(markdown_content):
  html_content = markdown(markdown_content)
  return html_content


def extract_published_date(soup):
  comments = soup.find(text=lambda text: isinstance(text, Comment) and 'date:' in text)
  if not comments:
    return ''
  published_date = comments.split(':')[-1].strip() if comments else ''
  return published_date


def extract_description(soup):
  comments = soup.find(text=lambda text: isinstance(text, Comment) and 'description:' in text)
  description = comments.split(':')[-1].strip() if comments else ''
  return description


def extract_tags(soup) -> list[str]:
  comments = soup.find(text=lambda text: isinstance(text, Comment) and 'tags:' in text)
  tags = comments.split(':')[-1].strip() if comments else ''
  return tags.split(', ') if tags else []


def fetch_notes(file_name=None) -> list:
  articles = []
  directory = 'notes'

  for root, dirs, files in os.walk(directory):
    for file in files:
      if file.endswith('.md') and file != 'README.md':
        file_path = os.path.join(root, file)
        markdown_content = read_markdown_file(file_path)
        html_content = parse_html_content(markdown_content)
        soup = BeautifulSoup(html_content, 'html.parser')

        title = os.path.splitext(os.path.basename(file))[0]
        published_date = extract_published_date(soup)
        description = extract_description(soup)
        tags = extract_tags(soup)[:3]

        article = Note(title, file_path, published_date, description, tags, content=html_content)

        # If file_name is provided and matches the current file, return the note
        if file_name and file == file_name:
          return article

        articles.append(article)

  # If file_name is provided but not found, return None
  if file_name:
    return None

  return articles

import os

from bs4 import BeautifulSoup, Comment
from markdown2 import markdown

from portfolio.src.models.project import Project


class ProjectBase:
  NOTES_PER_PAGE = 6

  @staticmethod
  def read_markdown_file(file_path):
    with open(file_path, 'r') as f:
      markdown_content = f.read()
    return markdown_content

  @staticmethod
  def parse_html_content(markdown_content):
    html_content = markdown(markdown_content)
    return html_content

  def extract_date(self, soup):
    comments = soup.find(text=lambda text: isinstance(text, Comment) and 'date:' in text)
    if not comments:
      return ''
    published_date = comments.split(':')[-1].strip() if comments else ''
    return published_date

  def extract_description(self, soup):
    comments = soup.find(text=lambda text: isinstance(text, Comment) and 'description:' in text)
    description = comments.split(':')[-1].strip() if comments else ''
    return description

  def extract_status(self, soup):
    comments = soup.find(text=lambda text: isinstance(text, Comment) and 'status:' in text)
    status = comments.split(':')[-1].strip() if comments else ''
    return status

  def extract_team_size(self, soup) -> int:
    comments = soup.find(text=lambda text: isinstance(text, Comment) and 'team_size:' in text)
    team_size = int(comments.split(':')[-1].strip()) if comments else 1
    return team_size

  def fetch_projects(self, file_name=None):
    articles = []
    directory = 'projects'

    for file in os.listdir(directory):
      file_path = os.path.join(directory, file)

      markdown_content = ProjectBase.read_markdown_file(file_path)
      html_content = ProjectBase.parse_html_content(markdown_content)
      soup = BeautifulSoup(html_content, 'html.parser')

      title = os.path.splitext(os.path.basename(file))[0]
      date = self.extract_date(soup) or '09 Mar, 2024'
      status = self.extract_status(soup) or 'on-going'
      team_size = self.extract_team_size(soup) or 1
      description = self.extract_description(soup) or 'view detail...'

      article = Project(title, date, description, status, team_size, content=html_content)

      # If file_name is provided and matches the current file, return the note
      if file_name and file == file_name:
        return article

      articles.append(article)

    # If file_name is provided but not found, return None
    if file_name:
      return None

    return articles


ProjectService = ProjectBase()

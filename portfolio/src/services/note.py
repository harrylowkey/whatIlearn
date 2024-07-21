import os
from datetime import datetime

from bs4 import BeautifulSoup, Comment
from markdown import markdown
from markdown.extensions.fenced_code import FencedCodeExtension

from portfolio.src.models.note import Note


class NoteBase:
  NOTES_PER_PAGE = 6

  @staticmethod
  def read_markdown_file(file_path):
    with open(file_path, 'r') as f:
      markdown_content = f.read()
    return markdown_content

  @staticmethod
  def parse_html_content(markdown_content):
    html_content = markdown(markdown_content, extensions=[FencedCodeExtension()])
    return html_content

  def extract_published_date(self, soup):
    comments = soup.find(text=lambda text: isinstance(text, Comment) and 'date:' in text)
    if not comments:
      return ''
    published_date = comments.split(':')[-1].strip() if comments else ''
    return published_date

  def extract_description(self, soup):
    comments = soup.find(text=lambda text: isinstance(text, Comment) and 'description:' in text)
    description = comments.split(':')[-1].strip() if comments else ''
    return description

  def extract_tags(self, soup) -> list[str]:
    comments = soup.find(text=lambda text: isinstance(text, Comment) and 'tags:' in text)
    tags = comments.split(':')[-1].strip() if comments else ''
    return tags.split(', ') if tags else []

  def calculate_title(self, path: str, file: str):
    segments = path.split('/')
    last_two_segments = segments[-2:]

    prefix_title =  '-'.join(list(filter(lambda segment: segment != 'notes', last_two_segments)))

    note_name = os.path.splitext(os.path.basename(file))[0]
    return f'{prefix_title}: {note_name}', note_name 

  def fetch_notes(self, file_name=None) -> list[Note] | Note:
    notes = []
    directory = 'notes'

    for root, dirs, files in os.walk(directory):
      for file in files:
        if file.endswith('.md') and file != 'README.md':
          file_path = os.path.join(root, file)

          markdown_content = NoteService.read_markdown_file(file_path)
          html_content = NoteService.parse_html_content(markdown_content)
          soup = BeautifulSoup(html_content, 'html.parser')

          title, original_title = self.calculate_title(root, file)
          published_date = self.extract_published_date(soup) or '09 Mar, 2024'
          description = self.extract_description(soup)
          tags = self.extract_tags(soup)[:3]

          note = Note(title, original_title, file_path, published_date, description, tags, content=html_content)

          if file_name and file == file_name:
            return note

          notes.append(note)

    if file_name:
      return None

    return notes

  def parse_date(self, date_str: str):
    return datetime.strptime(date_str, '%d %b, %Y')

  def paginate(self, page, key: str | None):
    notes: list[Note] = self.fetch_notes()

    if key:
      notes = [note for note in notes if key in note.title.lower()]

    total_notes = len(notes)
    start_idx = (page - 1) * NoteService.NOTES_PER_PAGE
    end_idx = start_idx + NoteService.NOTES_PER_PAGE

    prev_page = page - 1 if page > 1 else None
    next_page = page + 1 if end_idx < total_notes else None

    notes = sorted(notes, key=lambda note: self.parse_date(note.published_date), reverse=True)
    notes = notes[start_idx:end_idx]

    return notes, total_notes, prev_page, next_page


NoteService = NoteBase()

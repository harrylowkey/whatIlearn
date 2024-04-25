class Project:
  def __init__(self, title, date, description, status, team_size, is_highlight, content):
    self.date = date
    self.title = title
    self.status = status
    self.content = content
    self.team_size = team_size
    self.description = description
    self.is_highlight = is_highlight

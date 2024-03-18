class Note:
  def __init__(self, title, file_path, published_date, description, tags, content):
    self.title = title
    self.file_path = file_path
    self.description = description
    self.content = content
    self.tags = tags
    self.published_date = published_date

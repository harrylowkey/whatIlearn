from dataclasses import dataclass


@dataclass()
class Note:
  title: str
  original_title: str
  file_path: str
  published_date: str
  description: str
  tags: str
  content: str

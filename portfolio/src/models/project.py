from dataclasses import dataclass


@dataclass()
class Project:
  title: str
  date: str
  description: str
  status: str
  team_size: str
  is_highlight: bool
  content: str

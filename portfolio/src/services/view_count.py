from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
VIEW_COUNT_FILE = 'view_counts.txt'

class PageView(BaseModel):
    page: str
    count: int

def update_view_count(page):
    view_counts = read_view_counts()
    view_counts[page] = view_counts.get(page, 0) + 1
    write_view_counts(view_counts)

def get_view_count(page):
    view_counts = read_view_counts()
    return view_counts.get(page, 0)

def read_view_counts():
    try:
        with open(VIEW_COUNT_FILE, 'r') as file:
            view_counts = {}
            for line in file:
                page, count = line.strip().split(':')
                view_counts[page] = int(count)
            return view_counts
    except FileNotFoundError:
        return {}

def write_view_counts(view_counts):
    with open(VIEW_COUNT_FILE, 'w') as file:
        for page, count in view_counts.items():
            file.write(f"{page}:{count}\n")

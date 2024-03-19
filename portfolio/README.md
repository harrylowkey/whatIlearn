# Table of Contents

## Motivation

I want to do everything as code, so I usually schedule and plan my tasks every day in a markdown file.
To make it easier to check my tasks every day, I want something that can remind me daily to stay on track.

So that I've built a chatbot that sends my tasks to Slack.
Ideally, I want it to remind me before my tasks are due, but for now, it just notifies me daily at 9:00 AM, which is okay for now.

However, I want something more.
I want to visualize my tasks in a better way, so I was planing to build a simple website for that.
Additionally, I want to show my current notes on the website too, hoping it will help someone.

Currently, I'm hosting the website at http://harrylowkey.online

## Plan for future development

I hope we can contribute together to make this project better.

- [x] Still adding more notes after researching something new
- [ ] Build schedule-task-cli to add/upate tasks
- [ ] Build the better UI/UX for the website

## Requirements

- python3

## Installation

```
pip isntall -r portfolio/requirements.txt
```

```
cp portfolio/.env.example .env

## then pass you SLACK_TOKEN to .env
```

## Usage

```
uvicorn src.main:app --reload --port=3000
```

### Configure the time to let the bot remind you

edit the file `portfoliosrc/schedulers/send_task_scheduler.py`

### Adding More Notes
You can add more notes inside the notes directory. They will automatically appear in the "Notes" tab on the website.

### Adding Scheduled Tasks
To let the chatbot remind you of tasks, you need to add new tasks in the SCHEDULE.md file located in the portfolio directory.

Currently, the chatbot will remind you of:

High-priority tasks
Tasks scheduled for today
Tasks scheduled for yesterday
Here's the format for adding tasks:

```
All high-priority tasks must be defined below the following headers:
- Header h2 `## Backlogs`
- Header h3 `### High Priority Tasks`

All daily tasks must be defined below the following headers:
- Header h2 `## Tasks`
- Category by date below the header h4 `####`

- [ ] [task-type] (annotation) <task-description>

---

## Backlogs

### High Priority Tasks:

- [ ] [Work] Fix bug
- [x] [Side-project] Build Note pages

---

## Tasks

#### Mar-18

- [ ] [Reading] (Section 1) Design Pattern book
- [ ] [Learning] (Sections 1 - 4) AWS Developer Associate Certification
- [x] [Side-project] Build Task page

#### Mar-17

- [ ] [Reading] (Section 1) Design Pattern book
- [ ] [Learning] (Sections 1 - 4) AWS Developer Associate Certification
- [x] [Side-project] Create schedule-task-notification Slack bot
```

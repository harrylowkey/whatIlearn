#!/bin/sh

uvicorn schedule_tasks_bot.src.main:app --proxy-headers --forwarded-allow-ips='*' --host 0.0.0.0 --port 3000

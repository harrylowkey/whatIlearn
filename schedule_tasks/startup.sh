#!/bin/sh

uvicorn schedule_tasks.src.main:app --proxy-headers --forwarded-allow-ips='*' --host 0.0.0.0 --port 3000

# Comparition

1. Concurrency handling

- Event Emiiter: Customize event emitter
- Celery queue (support synchronous task) -> customize queue to support asynchronous task
- FastAPI: Synchronous lib -> using thread to prevent blocking main thread
- Database session:
 - Concurrency database queries (asyncio.gather) -> inject different sessions for each queries
 - Transaction: need to use the same session across request
 + Solution: using nested session (just an idea, not implement to test)
             inject different sessions for each queries



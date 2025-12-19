"""Solution file"""
import threading
import asyncio

def worker_function():
    return "completed"

async def async_worker():
    await asyncio.sleep(0.001)
    return "completed"

class ThreadPool:
    def __init__(self, workers=4):
        self.workers = workers

    def map(self, func, items):
        threads = []
        results = []
        for item in items:
            t = threading.Thread(target=lambda: results.append(func(item)))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        return results

"""Exercise 37: Context Managers"""
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

class GPUMemoryManager:
    def __init__(self, device_id):
        self.device_id = device_id

    def __enter__(self):
        print(f"Allocating GPU {self.device_id}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Releasing GPU {self.device_id}")

from contextlib import contextmanager

@contextmanager
def training_mode():
    print("Entering training mode")
    yield
    print("Exiting training mode")

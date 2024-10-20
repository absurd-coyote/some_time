import json
from abc import ABC, abstractmethod

from outputs.output_memory_port import OutputMemoryPort

class CookieMemoryAdapter(OutputMemoryPort):
    def __init__(self, store):
        super().__init__()
        self.store = store

    def save(self, status):
        self.store["data"] = json.dumps(status)

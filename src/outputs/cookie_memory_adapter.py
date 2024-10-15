import json
from abc import ABC, abstractmethod

from inputs.output_memory_port import OutputMemoryPort

class CookieMemoryAdapter(OutputMemoryPort):
    def __init__(self, store):
        self.time_counter = None
        self.store = store

    def init_time_counter(self, time_counter):
        self.time_counter = time_counter

    def save(self, status):
        self.store["data"] = json.dumps(status)

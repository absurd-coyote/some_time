import datetime
import json
from pyscript import storage

from inputs.input_memory_port import InputMemoryPort
    
class CookieMemoryAdapter(InputMemoryPort):
    def __init__(self, store):
        super().__init__()
        self.store = store

    def available(self):
        return "data" in self.store

    def load_values(self):
        status = json.loads(self.store["data"])
        counter = datetime.timedelta(seconds=status["counter"])
        counter_running = status["counter_running"]
        start_count = datetime.datetime.fromisoformat(status["start_count"])
        return counter, counter_running, start_count



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
        return json.loads(self.store["data"])



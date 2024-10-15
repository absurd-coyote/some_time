from pyscript import storage

from inputs.input_memory_port import InputMemoryPort
    
class CookieMemoryAdapter(InputMemoryPort):
    def __init__(self, store):
        self.time_counter = None
        self.store = store

    def init_time_counter(self, time_counter):
        self.time_counter = time_counter

    def available(self):
        return "data" in store

    def load_values(self, text):
        status = json.loads(self.store["data"])
        counter = datetime.timedelta(seconds=status["counter"])
        counter_running = status["counter_running"]
        start_count = datetime.datetime.fromisoformat(status["start_count"])
        return counter, counter_running, start_count



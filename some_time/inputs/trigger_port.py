
from abc import ABC, abstractmethod

class TriggerPort(ABC):
    def __init__(self):
        self.time_counter = None

    def init_time_counter(self, time_counter):
        self.time_counter = time_counter

    def start(self):
        self.time_counter.start()

    def stop(self):
        self.time_counter.stop()

    def reset(self):
        self.time_counter.reset()

    @abstractmethod
    def add_time(self, time_to_add):
        pass

    @abstractmethod
    def remove_time(self, time_to_remove):
        pass

    def _add_time(self, time_to_add):
        self.time_counter.add_time(time_to_add)

    def _remove_time(self, time_to_remove):
        self.time_counter.remove_time(time_to_remove)

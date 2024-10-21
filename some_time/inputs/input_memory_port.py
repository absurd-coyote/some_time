from abc import ABC, abstractmethod

class InputMemoryPort(ABC):
    def __init__(self):
        self.time_counter = None

    def init_time_counter(self, time_counter):
        self.time_counter = time_counter

    @abstractmethod
    def load_values(self):
        pass


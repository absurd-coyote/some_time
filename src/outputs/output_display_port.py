from abc import ABC, abstractmethod

class OutDisplayPort(ABC):
    def __init__(self):
        self.time_counter = None

    def init_time_counter(self, time_counter):
        self.time_counter = time_counter

    @abstractmethod
    def display(self, status):
        pass

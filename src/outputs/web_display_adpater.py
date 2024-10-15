from abc import ABC, abstractmethod

from pyscript import display

from outputs.output_display_port import OutDisplayPort

class WebDisplayAdapter(OutDisplayPort):
    def __init__(self):
        self.time_counter = None

    def init_time_counter(self, time_counter):
        self.time_counter = time_counter

    def display(self, counter):
        display(str(counter), target ="time", append=False)

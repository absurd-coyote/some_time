from abc import ABC, abstractmethod

from pyscript import display

from outputs.output_display_port import OutDisplayPort

class WebDisplayAdapter(OutDisplayPort):
    def __init__(self):
        super().__init__()

    def display(self, counter):
        display(str(counter), target ="time", append=False)

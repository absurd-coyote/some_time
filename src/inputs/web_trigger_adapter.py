from inputs.trigger_port import TriggerPort

class WebTriggerAdapter(TriggerPort):
    def __init__(self):
        super().__init__()

    def add_time(self, event):
        if event.target.id == "add-15":
            time_to_add = 15
        if event.target.id == "add-30":
            time_to_add = 30
        if event.target.id == "add-60":
            time_to_add = 60
        self._add_time(time_to_add)

    def remove_time(self):
        if event.target.id == "remove-15":
            time_to_remove = 15
        if event.target.id == "remove-30":
            time_to_remove = 30
        if event.target.id == "remove-60":
            time_to_remove = 60
        self._remove_time(time_to_remove)

    def _add_time(self, time_to_add):
        self.time_counter.add_time(time_to_add)

    def _remove_time(self, time_to_remove):
        self.time_counter.remove_time(time_to_remove)

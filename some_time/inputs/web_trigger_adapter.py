from some_time.inputs.trigger_port import TriggerPort

class WebTriggerAdapter(TriggerPort):
    def __init__(self):
        super().__init__()

    def add_time(self, event):
        if event.target.id == "add-15":
            time_to_add = 15
        elif event.target.id == "add-30":
            time_to_add = 30
        elif event.target.id == "add-60":
            time_to_add = 60
        else:
            raise ValueError(f"Unknown event {event}")
        self._add_time(time_to_add)

    def remove_time(self, event):
        if event.target.id == "remove-15":
            time_to_remove = 15
        elif event.target.id == "remove-30":
            time_to_remove = 30
        elif event.target.id == "remove-60":
            time_to_remove = 60
        else:
            raise ValueError(f"Unknown event {event}")
        self._remove_time(time_to_remove)

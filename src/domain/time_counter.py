import datetime


class TimeCounter:
    def __init__(self, input_trigger, input_memory, output_display, output_memory):
        self.input_trigger = input_trigger
        self.input_memory = input_memory
        self.output_display = output_display
        self.output_memory = output_memory
    
    def init(self):
        print("init")
        if self.input_memory.available():
            print("load_value")
            self.counter, self.counter_running, self.start_count = self.input_memory.load_values()
        else:
            print("default")
            self.counter = datetime.timedelta()
            self.counter_running = False
            self.start_count = 0
        print("done")

    def start(self):
        self.start_count = datetime.datetime.now()
        self.counter_running = True

    def stop(self):
        self.counter_running = False

    def reset(self):
        self.counter = datetime.timedelta()

    def add_time(self, time_to_add):
        self.counter += datetime.timedelta(seconds=time_to_add*60)

    def remove_time(self, time_to_remove):
        self.counter -= datetime.timedelta(seconds=time_to_remove*60)

    def update_time(self):
        now = datetime.datetime.now()
        if self.counter_running:
            self.counter += now - self.start_count
        self.start_count = now

        self.output_display.display(self.counter)
        self.output_memory.save({
            "counter": counter.total_seconds(),
            "counter_running": counter_running,
            "start_count": start_count.isoformat()
        })
            

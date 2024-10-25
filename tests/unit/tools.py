import threading
import time


class PeriodicRunner(threading.Thread):
    def __init__(self, target, period=5.0):
        threading.Thread.__init__(self, name='Sleeper')
        self.stop_event = threading.Event()
        self.target = target
        self.period = period

    def run(self):
        while not self.stop_event.is_set():
            start = time.time()
            self.target()
            end = time.time()
            duration = end - start
            remaining_for_period = max(0, self.period - duration)
            time.sleep(remaining_for_period)

    def stop(self):
        self.stop_event.set()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args, **kwargs):
        self.stop()
        print('Force set Thread Sleeper stop_event')



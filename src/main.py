from pyodide.ffi.wrappers import set_interval
from pyscript import storage

from domain.time_counter import TimeCounter
from inputs.cookie_memory_adapter import CookieMemoryAdapter as InputCookie
from inputs.web_trigger_adapter import WebTriggerAdapter
from outputs.cookie_memory_adapter import CookieMemoryAdapter as OutputCookie
from outputs.web_display_adapter import WebDisplayAdapter

store = await storage("some-time")

input_cookie = InputCookie(store)
web_trigger = WebTriggerAdapter()
output_cookie = OutputCookie(store)
web_display = WebDisplayAdapter()

time_counter = TimeCounter(web_trigger, input_cookie, web_display, output_cookie)

time_counter.init()
input_cookie.init_time_counter(time_counter)
web_trigger.init_time_counter(time_counter)
output_cookie.init_time_counter(time_counter)
web_display.init_time_counter(time_counter)

def add_time(event):
    web_trigger.add_time(event)

def remove_time(event):
    web_trigger.remove_time(event)

def start(event):
    web_trigger.start()

def stop(event):
    web_trigger.stop()

def reset(event):
    web_trigger.reset()

set_interval(time_counter.update_time, 10)

# import ltk
from pyweb import pydom
import datetime
import time
import asyncio
from pyodide.ffi.wrappers import set_interval

counter = 0
counter_running = False
start = 0

def start():
    start = datetime.datetime.now()
    counter_running = True
    

def update_time():
    if counter_running:
        now = datetime.datetime.now()
        pydom["div#time"].html = str(now - start)
    else:
        pydom["div#time"].html = str(counter)


set_interval(update_time, 10)


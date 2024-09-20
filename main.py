# import ltk
from pyweb import pydom
import datetime
import time
import asyncio
from pyodide.ffi.wrappers import set_interval

counter = 0
counter_running = False
start = 0

def start(event):
    global counter_running
    start = datetime.datetime.now()
    counter_running = True
    pydom["div#debug1"].html = "call start"
    

def update_time():
    global counter_running
    pydom["div#debug2"].html = str(counter_running)
    if counter_running:
        now = datetime.datetime.now()
        pydom["div#time"].html = str(now - start)
    else:
        pydom["div#time"].html = str(counter)


set_interval(update_time, 10)


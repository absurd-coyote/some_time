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
    global start
    start = datetime.datetime.now()
    counter_running = True
    pydom["div#debug1"].html = "call start"
    

def update_time():
    global counter_running
    global start
    pydom["div#debug2"].html = str(counter_running)
    if counter_running:
        pydom["div#debug3"].html = "up"
        now = datetime.datetime.now()
        pydom["div#time"].html = str(now - start)
    else:
        pydom["div#debug3"].html = "reset"
        pydom["div#time"].html = str(counter)


set_interval(update_time, 10)


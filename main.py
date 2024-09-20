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
    

def stop(event):
    global counter_running
    global start
    global counter

    counter_running = False
    now = datetime.datetime.now()
    counter += now - start


def update_time():
    global counter_running
    global start
    global counter

    if counter_running:
        now = datetime.datetime.now()
        pydom["div#time"].html = str(counter + now - start)
    else:
        pydom["div#time"].html = str(counter)


set_interval(update_time, 10)


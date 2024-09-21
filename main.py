# import ltk
from pyweb import pydom
import datetime
import time
import asyncio
from pyodide.ffi.wrappers import set_interval

counter = datetime.timedelta()
counter_running = False
start_count = 0


def start(event):
    global counter_running
    global start_count

    start_count = datetime.datetime.now()
    counter_running = True
    

def stop(event):
    global counter_running
    global start_count
    global counter

    counter_running = False
    now = datetime.datetime.now()
    counter += now - start_count


def reset(event):
    global counter
    counter = datetime.timedelta()


def add_time(event):
    global counter
    if event.target.id == "add-15":
        time_to_add = 15
    if event.target.id == "add-30":
        time_to_add = 30
    if event.target.id == "add-60":
        time_to_add = 60
    counter += datetime.timedelta(seconds=time_to_add*60)



def update_time():
    global counter_running
    global start_count
    global counter

    if counter_running:
        now = datetime.datetime.now()
        pydom["div#time"].html = str(counter + now - start_count)
    else:
        pydom["div#time"].html = str(counter)


set_interval(update_time, 10)


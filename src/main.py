import datetime
import time
import asyncio
import json
import sys
from pyodide.ffi.wrappers import set_interval
from pyscript import window
from pyscript import storage
from pyscript import display

import os


store = await storage("some-time")

counter = datetime.timedelta()
counter_running = False
start_count = 0

if "data" in store:
    status = json.loads(store["data"])
    counter = datetime.timedelta(seconds=status["counter"])
    counter_running = status["counter_running"]
    start_count = datetime.datetime.fromisoformat(status["start_count"])


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


def remove_time(event):
    global counter
    if event.target.id == "remove-15":
        time_to_remove = 15
    if event.target.id == "remove-30":
        time_to_remove = 30
    if event.target.id == "remove-60":
        time_to_remove = 60
    counter -= datetime.timedelta(seconds=time_to_remove*60)


async def update_time():
    global counter_running
    global start_count
    global counter

    now = datetime.datetime.now()
    if counter_running:
        counter += now - start_count

    start_count = now
    display(str(counter), target ="time", append=False)

    status = {
            "counter": counter.total_seconds(),
            "counter_running": counter_running,
            "start_count": start_count.isoformat()
            }
    dumpy = json.dumps(status)
    store["data"] =  dumpy

    print(sys.argv[0])
    # print(os.path.dirname(os.path.realpath(__file__)))
    # print(os.listdir(os.path.dirname(os.path.realpath(__file__))))


set_interval(update_time, 10)

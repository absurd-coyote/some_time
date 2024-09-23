import datetime
import time
import asyncio
import json
import sys
from pyodide.ffi.wrappers import set_interval
from pyscript import window
from pyscript import storage
from pyscript import display

ls = window.localStorage
store = await storage("my-storage-name")

counter = datetime.timedelta()
counter_running = False
start_count = 0

print("init")
if "data" in sync:
    print(store["data"])

# if data := ls.getItem("data"):
#     print("loaded")
#     print(data)
#     status = json.loads(data)
#     counter = status.counter
#     counter_running = status.counter_running
#     start_count = status.start_count


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



def update_time():
    global counter_running
    global start_count
    global counter

    now = datetime.datetime.now()
    if counter_running:
        counter += now - start_count

    start_count = now
    display(str(counter), target ="time", append=False)

    status = {
            "counter": counter,
            "start_count": start_count
            }
    store["data"] = json.dumps(status)
    await store.sync()
    if "data" in sync:
        print(store["data"])



set_interval(update_time, 10)


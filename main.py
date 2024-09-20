# import ltk
from pyweb import pydom
import datetime
import time
import asyncio
from pyodide.ffi.wrappers import set_interval

start = datetime.datetime.now()

def update_time():
    now = datetime.datetime.now()
    pydom["div#time"].html = str(now - start)

set_interval(update_time, 10)


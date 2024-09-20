# import ltk
from pyweb import pydom
import datetime
import time
import asyncio
from pyodide.ffi.wrappers import set_interval

def update_time():
    now = datetime.datetime.now()
    pydom["div#time"].html = str(now)

set_interval(uodate_time, 10)



# (
#     ltk.VBox(
#         ltk.HBox(
#             ltk.Text("Hello"),
#             ltk.Button(
#                 "World", 
#                 lambda event: 
#                     ltk.find(".ltk-button, a")
#                         .css("color", "red")
#             )
#             .css("color", "blue")
#         )
#     )
#     .appendTo(ltk.window.document.body)
# )

# import ltk
from pyweb import pydom
import datetime
import time
import asyncio

# while True:
#     now = datetime.datetime.now()
#     pydom["div#time"].html = str(now)
#     await asyncio.sleep(1)

from datetime import datetime
import asyncio

async def clock_forever():
    while(True):
        now = datetime.now()
        Element('clock-output').write(f"{now.hour}:{now.minute:02}:{now.second:02}")
        await asyncio.sleep(1)

PyScript.loop.create_task(clock_forever())

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

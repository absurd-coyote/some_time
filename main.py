# import ltk
from pyweb import pydom
import datetime
import time
import asyncio

while True:
    now = datetime.datetime.now()
    pydom["div#time"].html = str(now)
    await asyncio.sleep(1)


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

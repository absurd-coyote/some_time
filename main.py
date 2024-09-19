# import ltk
from pyweb import pydom

pydom["div#time"].html = f"paf"

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

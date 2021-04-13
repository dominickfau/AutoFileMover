from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os, os.path
import json
import time

class AutoFileMover(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            source = os.path.join(folder_to_track, filename)
            new_destination = os.path.join(destination_folder, filename)
            os.rename(source, new_destination)


folder_to_track = ""
destination_folder = ""

event_handler = AutoFileMover()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import file_manager as fm

import os
import json
import time

class Handler(FileSystemEventHandler):
    def on_any_event(self, event):
        for filename in folder_to_track.list_of_files():
            src = '{}/{}'.format(folder_to_track.location, filename)
            new_destination = '{}/{}'.format(folder_detination.location, filename)
            print('file: {}  move to: {}'.format(filename, new_destination))
            os.replace(src, new_destination)


folder_to_track = fm.Folder("C:/test_folder/folder_to_track")
folder_detination = fm.Folder("C:/test_folder/folder_detination")
file_to_track = fm.File("C:/test_folder/folder_to_track/Teste.txt")        

event_handler = Handler()

observer = Observer()
observer.schedule(event_handler, folder_to_track.location, recursive = True)
observer.start()

try:
    while True:    
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()


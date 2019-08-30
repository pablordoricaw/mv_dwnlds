from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time
from pathlib import Path

import utils

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        global folder_to_track

        folder_to_track = folder_to_track + '/' if folder_to_track[-1] != '/' else folder_to_track

        for file_name in os.listdir(folder_to_track):
            f = File(file_name)
            if f.get_file_name() != ignore_file.get_file_name():
                temp_folder_destination = folder_destination + f.get_file_type()[1:]
                temp_folder_destination = temp_folder_destination + '/' if temp_folder_destination[-1] != '/' else temp_folder_destination
                Path(temp_folder_destination).mkdir(exist_ok=True)

                src = folder_to_track + f.get_file_name()
                new_destination = temp_folder_destination + f.get_file_name()

                os.rename(src, new_destination)

class File():
    def __init__(self, file_name):
        self._file_name = file_name

    def get_file_name(self):
        return self._file_name

    def get_file_type(self):
        return Path(self._file_name).suffix

if __name__ == "__main__":
    d = os.path.dirname(os.path.abspath(__file__))
    config = utils.read_config(os.path.join(d, './config.yml'))

    global folder_to_track
    global folder_destination
    global ignore_file

    folder_to_track = config['track_dir']
    folder_destination = config['dst_dir']
    ignore_file_name = config['ignore_file']
    ignore_file = File(ignore_file_name)

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_track, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

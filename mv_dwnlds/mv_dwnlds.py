from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from os import listdir, rename
from os.path import dirname, abspath, join, exists
from re import search
import time
from pathlib import Path
from sys import exit

from utils import read_config, cleanup

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        global folder_to_track

        folder_to_track = folder_to_track + '/' if folder_to_track[-1] != '/' else folder_to_track

        for file_name in listdir(folder_to_track):
            f = File(file_name)
            if f.is_downloaded():
                if f.get_file_name() not in ignore_files_names:
                    temp_folder_destination = folder_destination + f.get_file_type()[1:]
                    temp_folder_destination = temp_folder_destination + '/' if temp_folder_destination[-1] != '/' else temp_folder_destination
                    Path(temp_folder_destination).mkdir(parents=True, exist_ok=True)

                    src = folder_to_track + f.get_file_name()
                    new_destination = temp_folder_destination + f.get_file_name()
                    
                    while exists(new_destination):
                        f.append_num()
                        new_destination = temp_folder_destination + f.get_file_name()

                    rename(src, new_destination)
        cleanup(folder_destination)

class File():
    def __init__(self, file_name):
        self._file_name = file_name

    def get_file_name(self):
        return self._file_name

    def get_file_type(self):
        return Path(self._file_name).suffix

    def append_num(self):
        match = search("-\d+\.", self._file_name)
        if match:
            match_num = search("\d+", self._file_name)
            old_num = match_num.group(0)
            self._file_name = self._file_name.replace(old_num, str(int(old_num) + 1))
        else:
            self._file_name = self._file_name.replace(".", "-1.")

    def is_downloaded(self):
        return True if not (self.get_file_name().endswith(".crdownload") or
            self.get_file_name().startswith(".com.google.Chrome") or
            self.get_file_name().endswith(".download")) else False

if __name__ == "__main__":
    d = dirname(dirname(abspath(__file__)))
    config = read_config(join(d, './config.yml'))

    global folder_to_track
    global folder_destination
    global ignore_files_names

    folder_to_track = config['track_dir']
    folder_destination = config['dst_dir']
    ignore_files_names = config['ignore_files']

    if folder_to_track == folder_destination:
        exit("[ERROR]: The track_dir and dst_dir in the config.yml file can NOT be the same directory")


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

import yaml
import errno
from os import listdir, rmdir, path
from shutil import rmtree

def read_config(config_file_path):
    with open(config_file_path) as config_file:
        data = yaml.load(config_file, Loader=yaml.FullLoader)
    return data

def cleanup(folder):
    ls = listdir(folder)
    ls = map(lambda f: path.join(folder, f), ls)
    folders = list(filter(lambda f: path.isdir(f), ls))
    for fldr in folders:
        ls_fldr = listdir(fldr)
        if not ls_fldr or (len(ls_fldr) == 1 and ls_fldr[0] == ".DS_Store"):
            try:
                rmtree(fldr)
            except OSError as e:
                if e.errno != errno.ENOTEMPTY:
                    raise


from os.path import dirname, abspath, join
from os import getcwd
from plistlib import dump

import utils

def write_plist(plist_path, plist_name, python_env):
    plist = dict(
        Label="plist_name",
        WorkingDirectory= dirname(abspath(__file__)) + "/",
        ProgramArguments= [
            python_env,
            "mv_dwnlds.py"
        ],
        RunAtLoad=True,
        KeepAlive=True
    )
    plist_file_name = plist_name + ".plist"
    plist_file_path = join(plist_path, plist_file_name)

    with open(plist_file_path, "wb") as fp:
        dump(plist, fp)

if __name__ == "__main__":
    d = dirname(dirname(abspath(__file__)))
    config = utils.read_config(join(d, './config.yml'))

    plist_name = config["plist_name"]
    python_env = config["python_env"]
    launch_agent_dir = config["launch_agent_dir"]

    write_plist(launch_agent_dir, plist_name, python_env)
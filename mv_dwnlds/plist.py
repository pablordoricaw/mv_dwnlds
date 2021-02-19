import os
from plistlib import dump

import utils

if __name__ == "__main__":
    d = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config = utils.read_config(os.path.join(d, './config.yml'))

    plist_name = config["plist_name"]
    python_env = config["python_env"]

    plist = dict(
        Label="plist_name",
        WorkingDirectory=os.getcwd() + "/",
        ProgramArguments= [
            python_env,
            "mv_dwnlds.py"
        ],
        RunAtLoad=True,
        KeepAlive=True
    )

    with open(plist_name + ".plist", "wb") as fp:
        dump(plist, fp)
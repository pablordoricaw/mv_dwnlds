from os.path import dirname, abspath, join, exists
from os import getcwd, system, remove
from pathlib import Path
from plistlib import dump
import argparse

from utils import read_config

def parse_args():
    parser = argparse.ArgumentParser()

    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument("-l", "--load", action="store_true", help="load agent")
    group1.add_argument("-u", "--unload", action="store_true", help="unload agent")

    group2 = parser.add_mutually_exclusive_group()
    group2.add_argument("--start", action="store_true", help="start loaded agent")
    group2.add_argument("--stop", action="store_true", help="stop loaded agent")

    parser.add_argument("-w", "--write", action="store_true", help="write plist file")
    parser.add_argument("--rm", action="store_true", help="rm plist file")
    parser.add_argument("--status", action="store_true", help="status of agent")
    return parser.parse_args()

def write_plist(plist_file_path, agent_name, python_env):
    plist = dict(
        Label=agent_name,
        WorkingDirectory= dirname(abspath(__file__)) + "/",
        ProgramArguments= [
            python_env,
            "mv_dwnlds.py"
        ],
        RunAtLoad=True,
        KeepAlive=True
    )
    
    Path(dirname(plist_file_path)).mkdir(parents=True, exist_ok=True)
    with open(plist_file_path, "wb") as fp:
        dump(plist, fp)

def status_agent(agent_name):
    system("launchctl list | grep " + agent_name)

def rm_plist(plist_file_path):
    remove(plist_file_path)

def load_agent(plist_file_path):
    system("launchctl load " + plist_file_path)

def unload_agent(plist_file_path):
    system("launchctl unload " + plist_file_path)

def start_agent(agent_name):
    system("launchctl start " + agent_name)

def stop_agent(agent_name):
    system("launchctl stop " + agent_name)

if __name__ == "__main__":
    
    args = parse_args()

    d = dirname(dirname(abspath(__file__)))
    config = read_config(join(d, './config.yml'))

    agent_name = config["plist_name"]
    python_env = config["python_env"]
    launch_agent_dir = config["launch_agent_dir"]

    plist_file_name = agent_name + ".plist"
    plist_file_path = join(launch_agent_dir, plist_file_name)

    if args.write:
        write_plist(plist_file_path, agent_name, python_env)
    if args.start:
        if not exists(plist_file_path):
            write_plist(plist_file_path, python_env)
        start_agent(agent_name)
    if args.stop:
        stop_agent(agent_name)
    if args.load:
        if not exists(plist_file_path):
            write_plist(plist_file_path, agent_name, python_env)
        load_agent(plist_file_path)
    if args.unload:
        unload_agent(plist_file_path)
    if args.status:
        status_agent(agent_name)
    if args.rm:
        rm_plist(plist_file_path)
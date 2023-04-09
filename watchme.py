import os
import signal
import sys
from time import sleep
from collections import defaultdict
from os.path import isfile, join
from os import walk
import json

with open('config.json') as config_file:
    data = json.load(config_file)

PORT = data["PORT"]
COMMAND = f"kill -kill $(netstat -vatn | rg {PORT} |" + r"awk '{ print $9 }' | head -1)"
RUN = data["script"]

def get_extension(filename):
    extentsion = filename.split(".")
    return extentsion[-1]

def get_time(file):
    fd = os.open(file, os.O_RDONLY)
    time = os.fstat(fd).st_mtime
    os.close(fd)
    return time

def get_all_paths(curr_path):
    paths = []
    extentions_to_watch = data["extensions"]
    for (dirpath, dirname, files) in os.walk(curr_path):
        for file in files:
            if(get_extension(file) in extentions_to_watch):
                paths.append(join(dirpath,file))
    return paths

def watch_changes(new_process):
    last_save_time = defaultdict(float)
    for i in range(10000):
        paths = get_all_paths(".")
        for file in paths:
            curr_save_time = get_time(file)
            if last_save_time.get(file, "Not found") == "Not found":
                last_save_time[file] = curr_save_time
                print(f"File {file} was created")
            if last_save_time[file] != curr_save_time:
                last_save_time[file] = curr_save_time
                print(f"File: {file} was changed")
                print(new_process)
                if new_process > 0 :
                    print(new_process)
                    print("Server killed")
                    os.kill(new_process, signal.SIGINT)
        sleep(1)
    
if __name__ == "__main__":
    new_process = os.fork()
    if new_process > 0 :
        os.system("node index.js")
        print(new_process)
    watch_changes(new_process)

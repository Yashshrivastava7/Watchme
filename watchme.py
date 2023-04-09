import os
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

def watch_changes(path):
    last_save_time = defaultdict(float)
    for i in range(10000):
        paths = get_all_paths(path)
        for file in paths:
            curr_save_time = get_time(file)
            if last_save_time.get(file, "Not found") == "Not found":
                last_save_time[file] = curr_save_time
                print(f"File {file} was created")
            if last_save_time[file] != curr_save_time:
                last_save_time[file] = curr_save_time
                try:
                    print("Running the commands")
                    os.system(COMMAND)
                    os.system(RUN)
                except e:
                    print("Errrr", e)
                print(f"File: {file} was changed")
        sleep(1)
    
if __name__ == "__main__":
    path = "."
    if len(sys.argv) == 2 :
        path = sys.argv[1]
    print(sys.argv)
    print(path)
    try:
        os.chdir(path)
        os.system(RUN)
    except e:
        print("Errrr", e)
    watch_changes(path)

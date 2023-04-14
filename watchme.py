import os
import multiprocessing
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
RUN = data["script"]
COMMAND = f"kill -kill $(netstat -vatn | rg {PORT} |" + r"awk '{ print $9 }' | head -1)"

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
    exclude = data["ignore directories"]
    for (dirpath, dirname, files) in os.walk(curr_path):
        [dirname.remove(d) for d in list(dirname) if d in exclude]
        for file in files:
            if(get_extension(file) in extentions_to_watch):
                paths.append(join(dirpath,file))
    return paths

def watch_changes(t1):
    last_save_time = defaultdict(float)
    for i in range(10000):
        is_changed = False
        paths = get_all_paths(".")
        for file in paths:
            curr_save_time = get_time(file)
            if last_save_time.get(file, "Not found") == "Not found":
                last_save_time[file] = curr_save_time
                print(f"File {file} was created")
            if last_save_time[file] != curr_save_time:
                is_changed = True
                last_save_time[file] = curr_save_time
                print(f"File: {file} was changed")
        if is_changed :
            print("lol")
            os.system(COMMAND)
            t1.terminate() 
            while t1.is_alive() :
                pass
            t1.close()
            t1 = multiprocessing.Process(target=os.system, args=[RUN])
            t1.start()
        sleep(1)
    
if __name__ == "__main__":
    t1 = multiprocessing.Process(target=os.system, args=[RUN])
    t1.start()
    watch_changes(t1)

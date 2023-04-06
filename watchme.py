import os
from time import sleep
from collections import defaultdict
from os.path import isfile, join
from os import walk

def get_time(file):
    fd = os.open(file, os.O_RDONLY)
    time = os.fstat(fd).st_mtime
    return time

def get_all_paths(curr_path):
    paths = []
    extentions_to_watch = {"cpp":1 , "ava":1, ".js":1, ".ts":1, "tsx":1, "jsx":1, "txt":1}
    for (dirpath, dirname, files) in os.walk(curr_path):
        for file in files:
            if(file[-3:] in extentions_to_watch):
                paths.append(join(dirpath,file))
    return paths

def watch_changes(paths):
    last_save_time = defaultdict(float)
    for i in range(100):
        for file in paths:
            curr_save_time = get_time(file)
            if last_save_time.get(file, "Not found") == "Not found":
                last_save_time[file] = curr_save_time
            if last_save_time[file] != curr_save_time:
                last_save_time[file] = curr_save_time
                print(f"File: {file} was changed")
        sleep(1)
    
if __name__ == "__main__":
    paths = get_all_paths(".")
    print(paths)

import os
from time import sleep
from os import listdir
from os.path import isfile, join
from os import walk
def get_all_files(curr_path):
   paths = []
   for path in listdir(curr_path):
       if isfile(join(curr_path,path)):
           paths.append(path)
   return paths        

def get_all_paths(curr_path):
    paths = []
    for (dirpath, dirname, files) in os.walk(curr_path):
        for file in files:
            paths.append(join(dirpath,file))
    return paths
   
if __name__ == "__main__":
    paths = get_all_paths(".")
    print(paths) 

import subprocess as sp
from os import chdir
from time import sleep

try:
    chdir("/Users/yashshrivastava/Documents/React/NotesApp-Backend/")
    p = sp.Popen(["npm", "run", "dev"])
    sleep(5)
    p1 = sp.Popen(["netstat", "-vatn"], stdout=sp.PIPE)
    p2 = sp.run(["rg", "8080"], stdin=p1.stdout)
except Exception as e:
    print("Exception:", e)
    

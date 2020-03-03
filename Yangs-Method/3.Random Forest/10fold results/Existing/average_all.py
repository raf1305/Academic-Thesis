import sys
import os
import glob

for file in glob.glob("*.txt"):
    print(file)
    os.system("python gg.py "+str(file))



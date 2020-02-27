import sys
import os
import glob

for file in glob.glob("*.csv"):
    print(file)
    os.system("python smote.py "+str(file))



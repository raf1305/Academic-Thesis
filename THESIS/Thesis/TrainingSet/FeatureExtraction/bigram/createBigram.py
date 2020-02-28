import os
import sys

start = int(sys.argv[1])
end = int(sys.argv[2])+1
_type = sys.argv[3]
for i in range(start, end):
    filename = str(i)+".FASTA.pssm"
    os.system("python probability.py " + filename)
    filename = str(i)+".prob.txt"
    os.system("python bigram.py " + filename + " " + _type)
    os.system("del " + filename)
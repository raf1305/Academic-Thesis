import sys
import os

start = int(sys.argv[1])
end = int(sys.argv[2])+1
for i in range(start,end):
	s  = str(i)+".FASTA"
	os.system("python 3gapDC.py "+s)
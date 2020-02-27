import os
import sys
import numpy as np
from io import StringIO
from numpy import linalg as LA
np.set_printoptions(suppress=True,precision=20)
#set your current directory



#take data form a text file
s = sys.argv[1]
words=s.split('.')
#file = open(s,"r")
#E=np.genfromtxt(StringIO(s), delimiter=',')
E = np.loadtxt(fname = s,dtype=float,delimiter=",")
#E=np.longdouble(E)
#print(E)

#transpose of E
Tranpose_E = np.transpose(E)
#print(Tranpose_E)

#multiplication of E and TE
PET = np.matmul(E,Tranpose_E)

#trace of PET
Tr = PET.trace()
#print(str(Tr)+'  '+s+'\n')
#divide PET by Tr to get 'R'
if (Tr==0.0):
    Tr=1
R = PET/Tr

np.savetxt(words[0]+'R.txt',R,'%10.50f')



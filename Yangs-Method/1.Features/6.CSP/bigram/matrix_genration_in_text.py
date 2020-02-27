import os
import sys
import numpy as np
from numpy import linalg as LA



s =sys.argv[1]
lin=int(sys.argv[2])

pro=[]
lines=[]
mat_row=[]
matrix=[]
total_lines=0
t_lines=0


with open(s) as f:
    f.readline()
    
    # print(t_lines)
    while True:
            
                line=f.readline()
                words=line.split(',')
                #print(words)
                pro.append(words)
                total_lines+=1
                if total_lines==lin:
                    break
    #print(total_lines)
    
    for i in range (0,total_lines-1):
        l=0
        s2 =str(i+1)+".txt"
        #print(s2+'\n')
        file = open(s2,"w")
        for j in range(0,400):
            #mat_row.append(float(pro[i][j]))
            file.write(pro[i][j])
            if(l<=18):
                file.write(',')
            l += 1
            if (l==20): 
                #print(mat_row)
                #matrix.append(mat_row)
                l=0
                #mat_row=[]
                file.write('\n')
        file.close()                 
        
        


        
               
        

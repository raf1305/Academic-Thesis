import sys
import pandas as pd
from math import pow
s = sys.argv[1]
_type = sys.argv[2]
words = s.split('.')
f = open(s)
num_lines = sum(1 for line in f)
amino_num = num_lines-1
#print(amino_num)
f.close()

f1=open('PSSM-ED-Trainingset.csv',"a+")

P = [[0 for x in range(20)] for y in range(num_lines-1)]
#print(P)
j = 0 
with open(s) as f:
    line = f.readline()
    aminoAcid = line.split()
    for i in range(amino_num):
        line = f.readline()
        P[i] = line.split()
        
# print(aminoAcid)
# for i in range(num_lines-1):
# print(P[i])
sum = 0
EDPSSM = pd.DataFrame(columns=aminoAcid)
#print(EDPSSM)


for m in range(20):
    sum = 0
    li = []
    for n in range(20):
        sum = 0
        for i in range(1,amino_num-1):
            sum += pow(float(P[i-1][m+1])-float(P[i+1][n+1]),2)
            # print(P[i][m+1]+" "+P[i+1][n+1]+" "+str(float(P[i][m+1])*float(P[i+1][n+1])))
        # file.write("\n\n")
        # file.write(aminoAcid[m]+aminoAcid[n]+" ")#+str(sum))
        # bigram[aminoAcid[m]+aminoAcid[n]] = sum
        
        sum = sum/(amino_num-2)
        f1.write(str(sum))
        f1.write(',')
    
f1.write(str(_type))
f1.write('\n')
        #li.append(sum)
    #EDPSSM[aminoAcid[m]] = li
# print bigram;
# print value;
# sortedKeys = sorted(bigram.keys())
# for i in sortedKeys:
    # file.write(str(bigram[i])+",")
# file.write(_type+"\n")
'''outputFile = ""
if(_type == '1'):
    outputFile += words[0]+"Cis-Golgi"+".csv"
elif(_type == '0'):
    outputFile += words[0]+"Trans-Golgi"+".csv"
EDPSSM.to_csv(outputFile,index=False)'''
f.close()

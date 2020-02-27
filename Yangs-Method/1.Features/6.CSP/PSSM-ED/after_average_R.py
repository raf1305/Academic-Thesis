import os
import sys
import numpy as np
from io import StringIO
from numpy import linalg as LA
#np.set_printoptions(suppress=True,precision=20)

s2=sys.argv[4]
f1=open(s2,"a+")

f1.write('A,R,N,D,C,Q,E,G,H,I,L,K,M,F,P,S,T,W,Y,V,class')
f1.write('\n')

average_cis=np.zeros((20,20))
average_trans=np.zeros((20,20))
start = int(sys.argv[1])
end = int(sys.argv[2])
end2 = int(sys.argv[3])
for i in range(start, end):
    filename = str(i)+"R.txt"
    E = np.loadtxt(fname = filename)
    average_cis=np.add(average_cis,E)
    os.system("del " + filename)
average_cis=average_cis/(end-1)
#np.savetxt('average_cis_R.txt',average_cis,'%10.30f')

for i in range(end, end2):
    filename = str(i)+"R.txt"
    E = np.loadtxt(fname = filename)
    average_trans=np.add(average_trans,E)
    os.system("del " + filename)
average_trans=average_trans/(end2-end)

#np.savetxt('average_trans_R.txt',average_trans,'%10.30f')

R_c=np.add(average_cis,average_trans)

ev, U = LA.eig(R_c)
Lemda_c = np.diag(ev)
Inv_Lemda_c=np.linalg.inv(Lemda_c)

#np.savetxt('lemda.txt',Inv_Lemda_c,'%10.30f')

Root_Inv_Lemda_c=np.sqrt(Inv_Lemda_c)

U_transpose=np.transpose(U)

P=np.matmul(Root_Inv_Lemda_c,U_transpose)
P_transpose=np.transpose(P)
S11=np.matmul(P,average_cis)
S1=np.matmul(S11,P_transpose)

S22=np.matmul(P,average_trans)
S2=np.matmul(S22,P_transpose)

S1_ev,B1=LA.eig(S1)
S2_ev,B2=LA.eig(S2)

#Lemda_1=np.diag(S1_ev)
#Lemda_2=np.diag(S2_ev)

#B=np.subtract(B1,B2)
#np.savetxt('B1-B2.txt',B,'%10.3f'

#It should be zero...but its not

#Lemda=np.add(Lemda_1,Lemda_2)
#np.savetxt('Lemda_1+2.txt',Lemda,'%10.30f')

B1_transpose=np.transpose(B1)
B2_transpose=np.transpose(B2)
WW=np.matmul(B1_transpose,P)
W=np.transpose(WW)

#generateWE
for i in range(start, end):
    filename = str(i)+".txt"
    E = np.loadtxt(fname = filename,dtype=float,delimiter=",")
    os.system("del " + filename)
    E1=np.matmul(W,E)
    #print(E1)
    #print('E1 var',E1.var(0))
    var_sum=0
    #np.savetxt('Z.txt',E1,'%10.30f')
    for i in range (1,21):
        x=E1[:,i-1]
        #print(x.var(0))
        var_sum+=x.var(0)
    if (var_sum==0.0):
        var_sum=1
    for i in range (1,21):
        x=E1[:,i-1]
        x1=x.var(0)
        x2=x1/var_sum
        if (x2==0):
            x2=1
        x3=np.log10(x2)
        f1.write(str(x3))
        f1.write(',')
    f1.write('0')
    f1.write('\n')
    
for i in range(end, end2):
    filename = str(i)+".txt"
    E = np.loadtxt(fname = filename,dtype=float,delimiter=",")
    os.system("del " + filename)
    E1=np.matmul(W,E)
    #print(E1)
    #print('E1 var',E1.var(0))
    var_sum=0
    #np.savetxt('Z.txt',E1,'%10.30f')
    for i in range (1,21):
        x=E1[:,i-1]
        #print(x.var(0))
        var_sum+=x.var(0)
    if (var_sum==0.0):
        var_sum=1
    for i in range (1,21):
        x=E1[:,i-1]
        x1=x.var(0)
        x2=x1/var_sum
        if (x2==0):
            x2=1
        x3=np.log10(x2)
        f1.write(str(x3))
        f1.write(',')
    f1.write('1')
    f1.write('\n')        
 

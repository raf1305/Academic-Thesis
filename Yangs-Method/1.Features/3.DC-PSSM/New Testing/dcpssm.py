import sys
s = sys.argv[1]
words=s.split('.')
t=sys.argv[2]
s2='PSSM-DC-Testingset-DIV-new.csv'
f1=open(s2,"a+")
with open(s) as f:
    
        line=f.readline()
        protein=line.split()
        #print(protein)
        total_lines=0
        pro=[]
        pssm=[]
        while True:
            
                line=f.readline()
                words=line.split()
                pro.append(words)
                total_lines+=1
                if words==[]:
                        break
        
        #print(total_lines)
        
        for i in range(0,20):
                for k in range(0,20):
                        sum=0
                        fre=0
                        for j in range(1,total_lines-1):
                
                                if(pro[j][0]==protein[i]):
                                        sum+=float(pro[j][k+1])
                                        fre+=1
                        #print(protein[i]+protein[k])
                        if(fre !=0):
                                sum=sum/fre
                        #print(sum)
                        f1.write(str(sum))
                        f1.write(',')
f1.write(t)
f1.write('\n')
f.close()
f1.close()


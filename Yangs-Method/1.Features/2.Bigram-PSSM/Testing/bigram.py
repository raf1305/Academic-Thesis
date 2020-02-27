import sys
s = sys.argv[1]
t = sys.argv[2]
words = s.split('.')
s2 = "PSSM-bigram-Testingset.csv"
file = open(s2,"a+")
f = open(s)
num_lines = sum(1 for line in f)
amino_num = num_lines-1
f.close()
P = [[0 for x in range(20)] for y in range(num_lines-1)]
j = 0 
with open(s) as f:
	line = f.readline()
	aminoAcid = line.split()
	for i in range(amino_num):
		line = f.readline()
		P[i] = line.split()
#for i in range(num_lines-1):
#	print(P[i])
sum = 0
bigram = {}
for m in range(20):
	sum = 0
	for n in range(20):
		sum = 0
		for i in range(amino_num-1):
			sum += float(P[i][m+1])*float(P[i+1][n+1])
			#print(P[i][m+1]+" "+P[i+1][n+1]+" "+str(float(P[i][m+1])*float(P[i+1][n+1])))
		#file.write("\n\n")
		#file.write(aminoAcid[m]+aminoAcid[n]+" ")#+str(sum))
		bigram[aminoAcid[m]+aminoAcid[n]] = sum
#print bigram;
#print value;
sortedKeys = sorted(bigram.keys())
for i in sortedKeys:
	file.write(str(bigram[i])+",")
file.write(t+"\n")	
f.close()
file.close()						

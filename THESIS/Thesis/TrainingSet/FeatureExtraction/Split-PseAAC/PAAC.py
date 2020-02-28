import sys
#from propy.GetProteinFromUniprot import GetProteinSequence as gps
from propy.PyPro import GetProDes

input = sys.argv[1]
output = "PAAC.csv"
input_file = open(input,"r+")
output_file = open(output,"a+")
id = input_file.readline()
sequence = input_file.readline().rstrip()
#uniprotid = "P48039"
#proseq = gps(uniprotid)
#print(type(proseq))
#print(sequence)
print(sequence)
Des = GetProDes(sequence)
PAAC = Des.GetPAAC(lamda=46,weight=0.05)
for i in sorted(PAAC.keys()):
	output_file.write(str(PAAC[i])+",")
if "Cis-golgi".lower() in id.lower():
	output_file.write("1\n")
else:
	output_file.write("0\n")
print(input+" completed\n")


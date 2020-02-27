import sys
fileName = sys.argv[1]
gap_number=sys.argv[2]
input_file = open(fileName,"r+")
output_file = open(gap_number+"gapDCTestingset_new.csv","a+")
id = input_file.readline()
sequence = input_file.readline()
sequence = sequence.rstrip()
aminoacids = ["A","R","N","D","C","Q","E","G","H","I","L","K","M","F","P","S","T","W","Y","V"]
dictDipeptide = {}
dictAminoacid = {}
dictDC = {}
for i in aminoacids:
	for j in aminoacids:
		dictDipeptide[i+j] = 0.0

i = 0
gap = int(gap_number)
length = len(sequence)
for i in range(0,len(sequence)-gap-1):
	# dipeptide = sequence[i]+sequence[i+4]
	# dipeptide_count = float(sequence.count(dipeptide))
	# first_residue_count = float(sequence.count(sequence[i]))
	# second_residue_count = float(sequence.count(sequence[i+4]))
	# #print(dipeptide_count,first_residue_count,second_residue_count)
	# result = float((dipeptide_count*100)/(first_residue_count*second_residue_count))
	# dict[dipeptide] = result
	dictDipeptide[sequence[i]+sequence[i+gap+1]] += 1
	
for dipeptide in dictDipeptide:
	dictDC[dipeptide] = dictDipeptide[dipeptide]/(length-gap-1)
#print(sys.argv[1]+str(len(dict)))
sortedKeys = sorted(dictDC.keys())
for key in sortedKeys:
	output_file.write(str(dictDC[key]))
	output_file.write(",")
if "Cis-Golgi".lower() in id.lower():
	output_file.write("0")
else:
	output_file.write("1")
output_file.write("\n")
output_file.close()
input_file.close()


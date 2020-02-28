import sys
inputfile_name = "output.txt"
outputfile_name = "TestingsetPAAC.csv"
outputfile = open(outputfile_name,"w+")
with open(inputfile_name,"r") as file:
	for line in file:
		if line != '\n':
			outputfile.write(line)
outputfile.close()
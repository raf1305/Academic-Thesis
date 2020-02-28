import sys
output_file = open("column.txt","w+")
aminoacids = ["A","R","N","D","C","Q","E","G","H","I","L","K","M","F","P","S","T","W","Y","V"]
dc = []
for i in aminoacids:
	for j in aminoacids:
		dc.append(i+j)
dc.sort()
for i in dc:
    output_file.write(i+",")
output_file.write("class")

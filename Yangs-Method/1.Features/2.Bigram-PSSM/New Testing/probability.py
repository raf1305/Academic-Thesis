import sys
s = sys.argv[1]
words = s.split('.')
s2 = words[0]+".prob.txt"
file = open(s2,"w")
print(s2)
with open(s) as f:
	f.readline()
	f.readline()
	line = f.readline()
	words = line.split()
	j = 0
	file.write("           ")
	for i in words:
		j += 1
		if j > 20:
			file.write(i+"         ")
	while True:
		line = f.readline()
		words = line.split()
		if words==[]:
			break
		j = 0	
		sum = 0
		file.write("\n")
		for i in words:
			j+=1
			if j > 22 and j < 43:
				sum += int(float(i))
		j = 0
		file.write("  "+words[1])
		file.write("       ")
		for i in words:
			j+=1
			if j > 22 and j < 43:
				if(sum==0):
					file.write(str(float(sum))+"        ")
				else:
					file.write(str(float(i)/float(sum))+"        ")
f.close()
file.close()						

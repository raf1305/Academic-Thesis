import csv

#3gap+DC
with open('3gapDCTestingset.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent1 = list(reader)

for row in csvContent1:
    del row[400] 
	
with open('CSP-PSSM-DC-Testingset-DIV.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent2 = list(reader)
	
result = [a+b for (a,b) in zip(csvContent1, csvContent2)]

with open('3-gap+CSP-DC.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)


#3gap+ED
with open('3gapDCTestingset.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent1 = list(reader)

for row in csvContent1:
    del row[400] 
	
with open('CSP-PSSM-ED-Testingset.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent2 = list(reader)
	
result = [a+b for (a,b) in zip(csvContent1, csvContent2)]

with open('3-gap+CSP-ED.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)

#3gap+bigram
with open('3gapDCTestingset.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent1 = list(reader)

for row in csvContent1:
    del row[400] 
	
with open('CSP-PSSM-bigram-Testingset.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent2 = list(reader)
	
result = [a+b for (a,b) in zip(csvContent1, csvContent2)]

with open('3-gap+CSP-Bigram.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)
#3gap+DC+ED
with open('3-gap+CSP-DC.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent1 = list(reader)

for row in csvContent1:
    del row[420] 
	
with open('CSP-PSSM-ED-Testingset.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent2 = list(reader)
	
result = [a+b for (a,b) in zip(csvContent1, csvContent2)]

with open('3-gap+CSP-DC+CSP-ED.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)
#3gap+DC+bigram
with open('3-gap+CSP-DC.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent1 = list(reader)

for row in csvContent1:
    del row[420] 
	
with open('CSP-PSSM-bigram-Testingset.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent2 = list(reader)
	
result = [a+b for (a,b) in zip(csvContent1, csvContent2)]

with open('3-gap+CSP-DC+CSP-bigram.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)

#3gap+bigram+ED
with open('3-gap+CSP-Bigram.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent1 = list(reader)

for row in csvContent1:
    del row[420] 
	
with open('CSP-PSSM-ED-Testingset.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent2 = list(reader)
	
result = [a+b for (a,b) in zip(csvContent1, csvContent2)]

with open('3-gap+CSP-bigram+CSP-ED.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)

#3gap+bigram+ED+DC

with open('3-gap+CSP-DC+CSP-bigram.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent1 = list(reader)

for row in csvContent1:
    del row[440] 
	
with open('CSP-PSSM-ED-Testingset.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent2 = list(reader)
	
result = [a+b for (a,b) in zip(csvContent1, csvContent2)]

with open('3-gap+CSP-bigram+CSP-DC+CSP-ED.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)

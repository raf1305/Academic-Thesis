import csv

#3gap+DC
with open('3gapDCTestingset-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent1 = list(reader)

for row in csvContent1:
    del row[400] 
	
with open('CSP-PSSM-DC-Testingset-DIV-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent2 = list(reader)
	
result = [a+b for (a,b) in zip(csvContent1, csvContent2)]

with open('3-gap+CSP-DC-new.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)


#3gap+ED
with open('3gapDCTestingset-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent1 = list(reader)

for row in csvContent1:
    del row[400] 
	
with open('CSP-PSSM-ED-Testingset-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent2 = list(reader)
	
result = [a+b for (a,b) in zip(csvContent1, csvContent2)]

with open('3-gap+CSP-ED-new.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)

#3gap+bigram
with open('3gapDCTestingset-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent1 = list(reader)

for row in csvContent1:
    del row[400] 
	
with open('CSP-PSSM-bigram-Testingset-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent2 = list(reader)
	
result = [a+b for (a,b) in zip(csvContent1, csvContent2)]

with open('3-gap+CSP-Bigram-new.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)
#3gap+DC+ED
with open('3-gap+CSP-DC-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent1 = list(reader)

for row in csvContent1:
    del row[420] 
	
with open('CSP-PSSM-ED-Testingset-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent2 = list(reader)
	
result = [a+b for (a,b) in zip(csvContent1, csvContent2)]

with open('3-gap+CSP-DC+CSP-ED-new.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)
#3gap+DC+bigram
with open('3-gap+CSP-DC-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent1 = list(reader)

for row in csvContent1:
    del row[420] 
	
with open('CSP-PSSM-bigram-Testingset-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent2 = list(reader)
	
result = [a+b for (a,b) in zip(csvContent1, csvContent2)]

with open('3-gap+CSP-DC+CSP-bigram-new.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)

#3gap+bigram+ED
with open('3-gap+CSP-Bigram-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent1 = list(reader)

for row in csvContent1:
    del row[420] 
	
with open('CSP-PSSM-ED-Testingset-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent2 = list(reader)
	
result = [a+b for (a,b) in zip(csvContent1, csvContent2)]

with open('3-gap+CSP-bigram+CSP-ED-new.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)

#3gap+bigram+ED+DC

with open('3-gap+CSP-DC+CSP-bigram-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent1 = list(reader)

for row in csvContent1:
    del row[440] 
	
with open('CSP-PSSM-ED-Testingset-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent2 = list(reader)
	
result = [a+b for (a,b) in zip(csvContent1, csvContent2)]

with open('3-gap+CSP-bigram+CSP-DC+CSP-ED-new.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)

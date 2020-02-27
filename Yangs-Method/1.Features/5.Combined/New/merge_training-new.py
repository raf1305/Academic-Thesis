import csv

#3gap+DC
with open('3gapDCTrainingset-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent1 = list(reader)

for row in csvContent1:
    del row[400] 
	
with open('CSP-PSSM-DC-Trainingset-DIV-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent2 = list(reader)
	
result = [a+b for (a,b) in zip(csvContent1, csvContent2)]

with open('3-gap+CSP-DC-training-new.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)


#3gap+ED
with open('3gapDCTrainingset-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent1 = list(reader)

for row in csvContent1:
    del row[400] 
	
with open('CSP-PSSM-ED-Trainingset-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent2 = list(reader)
	
result = [a+b for (a,b) in zip(csvContent1, csvContent2)]

with open('3-gap+CSP-ED-training-new.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)

#3gap+bigram
with open('3gapDCTrainingset-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent1 = list(reader)

for row in csvContent1:
    del row[400] 
	
with open('CSP-PSSM-bigram-Trainingset-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent2 = list(reader)
	
result = [a+b for (a,b) in zip(csvContent1, csvContent2)]

with open('3-gap+CSP-Bigram-training-new.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)
#3gap+DC+ED
with open('3-gap+CSP-DC-training-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent1 = list(reader)

for row in csvContent1:
    del row[420] 
	
with open('CSP-PSSM-ED-Trainingset-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent2 = list(reader)
	
result = [a+b for (a,b) in zip(csvContent1, csvContent2)]

with open('3-gap+CSP-DC+CSP-ED-training-new.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)
#3gap+DC+bigram
with open('3-gap+CSP-DC-training-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent1 = list(reader)

for row in csvContent1:
    del row[420] 
	
with open('CSP-PSSM-bigram-Trainingset-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent2 = list(reader)
	
result = [a+b for (a,b) in zip(csvContent1, csvContent2)]

with open('3-gap+CSP-DC+CSP-bigram-training-new.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)

#3gap+bigram+ED
with open('3-gap+CSP-Bigram-training-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent1 = list(reader)

for row in csvContent1:
    del row[420] 
	
with open('CSP-PSSM-ED-Trainingset-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent2 = list(reader)
	
result = [a+b for (a,b) in zip(csvContent1, csvContent2)]

with open('3-gap+CSP-bigram+CSP-ED-training-new.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)

#3gap+bigram+ED+DC

with open('3-gap+CSP-DC+CSP-bigram-training-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent1 = list(reader)

for row in csvContent1:
    del row[440] 
	
with open('CSP-PSSM-ED-Trainingset-new.csv', newline='') as f:
	reader = csv.reader(f)
	csvContent2 = list(reader)
	
result = [a+b for (a,b) in zip(csvContent1, csvContent2)]

with open('3-gap+CSP-bigram+CSP-DC+CSP-ED-training-new.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)
